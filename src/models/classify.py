from pydantic import BaseModel
from typing import Optional


class ClassifyRequest(BaseModel):
    text: Optional[str] = None


class ClassifyResponse(BaseModel):
    category: str
    confidence: float
    suggested_reply: str
