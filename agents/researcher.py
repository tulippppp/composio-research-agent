from google.genai import types

from models.app import AppResearch
from utils.gemini import client


SYSTEM_PROMPT = """
You are an API research analyst.

Research ONE application.

Use official developer documentation whenever possible.

Never fabricate information.

If something cannot be verified,
state that it is unknown.

Return structured JSON only.
"""


def research_app(app_name: str) -> AppResearch:

    prompt = f"""
Application:

{app_name}

Find:

- category
- one line description
- authentication methods
- self serve or gated
- why
- api type
- api scope
- mcp availability
- mcp details
- buildability
- blocker
- evidence urls
- confidence
"""

    response = client.models.generate_content(

        model="gemini-flash-latest",

        contents=prompt,

        config=types.GenerateContentConfig(

            system_instruction=SYSTEM_PROMPT,

            response_mime_type="application/json",

            response_schema=AppResearch,

            temperature=0.1,

        ),
    )

    return AppResearch.model_validate_json(response.text)