from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    max_results: int = 5
    source: str = "arxiv"  # "arxiv" or "scholar"

class UserActivity(BaseModel):
    user_id: str
    query: str
    source: str