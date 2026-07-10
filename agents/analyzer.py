import json
from pathlib import Path
from collections import Counter

VERIFIED_DIR = Path("data/verified")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)


NORMALIZE_AUTH = {
    "OAuth2": "OAuth 2.0",
    "OAuth 2.0": "OAuth 2.0",

    "API Key": "API Key",
    "API Keys": "API Key",

    "Bot Token": "Bot Token",
    "Bot Tokens": "Bot Token",

    "Personal Access Tokens": "Personal Access Token",
    "Personal Access Tokens (PATs)": "Personal Access Token",
}


def normalize(auth: str):
    return NORMALIZE_AUTH.get(auth, auth)


def analyze_results():

    auth_counter = Counter()
    category_counter = Counter()
    blocker_counter = Counter()

    apps = []

    total = 0
    self_serve = 0
    gated = 0
    mcp = 0
    buildable = 0

    for file in VERIFIED_DIR.glob("*.json"):

        with open(file) as f:
            app = json.load(f)

        apps.append(app)

        total += 1

        category_counter[app["category"]] += 1

        for auth in app["auth_methods"]:
            auth_counter[normalize(auth)] += 1

        blocker_counter[app["blocker"]] += 1

        if app["self_serve"]:
            self_serve += 1
        else:
            gated += 1

        if app["mcp_available"]:
            mcp += 1

        if app["buildable_today"]:
            buildable += 1
    top_auth = auth_counter.most_common(1)[0][0] if auth_counter else "Unknown"
    top_category = category_counter.most_common(1)[0][0] if category_counter else "Unknown"
    top_blocker = blocker_counter.most_common(1)[0][0] if blocker_counter else "None"

    insights = [
    f"The most common authentication method is {top_auth}.",
    f"The most common application category is {top_category}.",
    f"{self_serve} of {total} applications are self-service.",
    f"{mcp} of {total} applications provide MCP support.",
    f"The most common blocker is '{top_blocker}'.",
]
    summary = {
    "total_apps": total,
    "self_serve": self_serve,
    "gated": gated,
    "mcp_available": mcp,
    "buildable_today": buildable,
    "top_categories": dict(category_counter),
    "top_auth_methods": dict(auth_counter),
    "top_blockers": dict(blocker_counter),
    "insights": insights,
}

    with open(OUTPUT_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    with open(OUTPUT_DIR / "apps.json", "w") as f:
        json.dump(apps, f, indent=4)

    return summary