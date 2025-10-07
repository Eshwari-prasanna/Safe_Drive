import json
import os

DATA_FILE = "safedrive_data.json"

def load_data():
    """Load existing JSON data or create a new structured dictionary."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                d = json.load(f)
                if isinstance(d, dict) and all(k in d for k in ["vehicles", "drivers", "trips"]):
                    return d
        except json.JSONDecodeError:
            pass
    return {"vehicles": [], "drivers": [], "trips": []}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
