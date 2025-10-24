from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from detectors import detect_threat
from dotenv import load_dotenv
import os, time, json

load_dotenv()  # Load configs from .env

RATE_LIMIT = int(os.getenv("RATE_LIMIT", 10))  # max requests per minute
ALLOWED_IPS = os.getenv("ALLOWED_IPS", "").split(",")  # comma-separated IPs
API_KEYS = os.getenv("API_KEYS", "").split(",")  # comma-separated API keys

# Simple in-memory request tracking
request_counts = {}

class APIFirewallMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        client_ip = request.client.host

        # IP allowlist check
        if ALLOWED_IPS and client_ip not in ALLOWED_IPS:
            return JSONResponse({"detail": "IP not allowed"}, status_code=403)

        # Rate limiting
        current_time = time.time()
        if client_ip not in request_counts:
            request_counts[client_ip] = []
        # Remove requests older than 60 seconds
        request_counts[client_ip] = [t for t in request_counts[client_ip] if current_time - t < 60]
        if len(request_counts[client_ip]) >= RATE_LIMIT:
            return JSONResponse({"detail": "Rate limit exceeded"}, status_code=429)
        request_counts[client_ip].append(current_time)

        # API key check
        api_key = request.headers.get("x-api-key")
        if API_KEYS and api_key not in API_KEYS:
            return JSONResponse({"detail": "Invalid or missing API key"}, status_code=401)

        # Threat detection
        try:
            body = await request.body()
            data_str = body.decode("utf-8") if body else ""
        except Exception:
            data_str = ""

        full_data = f"{request.url} {request.headers} {data_str}"
        threat_type = detect_threat(full_data)

        if threat_type:
            with open("firewall_logs.txt", "a") as log:
                log.write(f"[{time.ctime()}] Blocked {threat_type} from {client_ip}\n")
            return JSONResponse({"detail": f"Request blocked by API Firewall: {threat_type}"}, status_code=403)

        response = await call_next(request)
        return response
