import time
from google.genai import types

from models.app import AppResearch
from utils.gemini import client


SYSTEM_PROMPT = """
You are a strict API verifier.

Your job is to verify an existing research report.

Do NOT invent information.

If evidence is weak,
lower the confidence.

If claims are unsupported,
correct them.

Return valid JSON only.
"""


def verify_app(app: AppResearch) -> AppResearch:

    prompt = f"""
Verify this application research.

Research:

{app.model_dump_json(indent=2)}

Check:

- Are the URLs valid?
- Are the claims supported?
- Is the API type correct?
- Is MCP availability correct?
- Is the confidence realistic?

Return corrected JSON.
"""

    last_exception = None

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    response_schema=AppResearch,
                    temperature=0,
                ),
            )
            break

        except Exception as e:
            last_exception = e
            print(f"Attempt {attempt + 1}/3 failed: {e}")

            if attempt < 2:
                print("Retrying in 5 seconds...")
                time.sleep(5)
    else:
        raise last_exception

    return AppResearch.model_validate_json(response.text)