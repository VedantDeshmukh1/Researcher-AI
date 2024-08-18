from pydantic import BaseModel
from typing import List, Optional

class Paper(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    published_date: str
    url: Optional[str] = None

class SearchRequest(BaseModel):
    query: str
    max_results: int = 10

class SearchResponse(BaseModel):
    papers: List[Paper]