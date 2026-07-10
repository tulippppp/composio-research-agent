from agents.researcher import research_app
from agents.verifier import verify_app
from agents.analyzer import analyze_results

from utils.io import (
    load_apps,
    save_result,
    save_verified,
    is_verified,
)

apps = load_apps("data/apps.csv")

for app_name in apps:

    if is_verified(app_name):
        print(f"Skipping {app_name} (already verified)")
        continue

    print(f"\nResearching {app_name}...")

    try:
        research = research_app(app_name)

        save_result(
            app_name,
            research.model_dump()
        )

        verified = verify_app(research)

        save_verified(
            app_name,
            verified.model_dump()
        )

        print(f"✅ Finished {app_name}")

    except Exception as e:
        print(f"Failed {app_name}")
        print(e)

print("\nAnalysis Summary\n")

summary = analyze_results()

print(summary)