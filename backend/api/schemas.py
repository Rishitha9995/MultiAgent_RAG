#schemas.py
from pydantic import BaseModel
from typing import List


class QueryRequest(BaseModel):
    """
    Request schema sent from the frontend (React UI)
    """
    query: str
    dataset: str


class QueryResponse(BaseModel):
    """
    Response returned to the frontend
    """
    corrected_query: str
    documents: List[str]
    answer: str