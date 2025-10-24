import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            path = os.path.join(root, file)
            with open(path, "rb") as f:
                content = f.read()
            if b"\x00" in content:
                print(f"Cleaning null bytes in: {path}")
                # Remove null bytes and overwrite the file
                content = content.replace(b"\x00", b"")
                with open(path, "wb") as f:
                    f.write(content)

print("All Python files cleaned of null bytes!")
