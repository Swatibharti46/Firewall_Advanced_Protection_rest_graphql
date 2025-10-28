from flask import Flask, render_template, jsonify
import random
import time

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static',
    template_folder='templates'
)

# --- Routes ---
@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/blocked')
def blocked():
    return render_template('blocked.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

# --- API for dynamic charts ---
@app.route('/api/stats')
def stats():
    data = {
        "allowed": random.randint(300, 800),
        "blocked": random.randint(50, 200),
        "latency": [random.randint(10, 50) for _ in range(6)],
        "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    }
    return jsonify(data)

@app.route('/api/logs')
def get_logs():
    sample_logs = [
        {"time": time.strftime("%H:%M:%S"), "ip": f"192.168.1.{random.randint(10,99)}", "status": "BLOCKED"},
        {"time": time.strftime("%H:%M:%S"), "ip": f"10.0.0.{random.randint(1,50)}", "status": "ALLOWED"}
    ]
    return jsonify(sample_logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
