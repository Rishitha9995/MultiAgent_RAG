#schemas.py
# from pydantic import BaseModel
# from typing import List, Dict, Any


# class QueryRequest(BaseModel):
#     query: str
#     dataset: str


# class Explanation(BaseModel):
#     rank: int
#     source: str
#     score: float
#     reason: str


# class QueryResponse(BaseModel):
#     corrected_query: str
#     dataset: str
#     answer: str
#     documents: List[str]
#     explanations: List[Explanation]
#     metrics: Dict[str, Any]
#     response_time: float

from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str
    dataset: Optional[str] = "business"   

class Explanation(BaseModel):
    rank: int
    source: str
    score: float
    reason: str

class QueryResponse(BaseModel):
    corrected_query: str
    dataset: str
    answer: str
    documents: List[str]
    explanations: List[Explanation]
    metrics: Dict[str, Any]
    response_time: float