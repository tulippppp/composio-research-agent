import json
import csv
from pathlib import Path


RAW_DIR = Path("data/raw")
VERIFIED_DIR = Path("data/verified")

VERIFIED_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)


def save_result(app_name: str, data: dict):
    filename = app_name.lower().replace(" ", "_") + ".json"

    with open(RAW_DIR / filename, "w") as f:
        json.dump(data, f, indent=4)

def save_verified(app_name: str, data: dict):
    filename = app_name.lower().replace(" ", "_") + ".json"

    with open(VERIFIED_DIR / filename, "w") as f:
        json.dump(data, f, indent=4)
        
def is_verified(app_name: str) -> bool:
    filename = app_name.lower().replace(" ", "_") + ".json"
    return (VERIFIED_DIR / filename).exists()

def load_apps(path: str) -> list[str]:
    apps = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            apps.append(row["name"])

    return apps