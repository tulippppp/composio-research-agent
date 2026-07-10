from typing import List, Optional

from pydantic import BaseModel, Field


class AppResearch(BaseModel):
    name: str = Field(description="Application name")

    category: str
    description: str

    auth_methods: List[str]

    self_serve: bool
    self_serve_reason: str

    api_type: List[str]
    api_scope: str

    mcp_available: bool
    mcp_details: Optional[str] = None

    buildable_today: bool
    blocker: str

    evidence: List[str]

    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence score between 0 and 1"
    )