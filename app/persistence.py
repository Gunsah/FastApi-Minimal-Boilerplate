import os

DATA_DIR = os.getenv("DATA_DIR", "/data")
os.makedirs(DATA_DIR, exist_ok=True)

def save_state(key: str, value: str):
    with open(os.path.join(DATA_DIR, f"{key}.txt"), "w") as f:
        f.write(value)

def load_state(key: str) -> str:
    path = os.path.join(DATA_DIR, f"{key}.txt")
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return ""
