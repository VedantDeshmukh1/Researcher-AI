from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import SearchRequest, UserActivity
from .services import arxiv_service, google_scholar_service
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

# ... (rest of your imports and app setup)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Researcher-AI API"}

@app.post("/search")
async def search_papers(request: SearchRequest):
    if request.source == "arxiv":
        papers = arxiv_service.search(request.query, request.max_results)
    elif request.source == "scholar":
        papers = google_scholar_service.search(request.query, request.max_results)
    else:
        raise ValueError("Invalid source")
    
    return papers

@app.post("/log_activity")
async def log_user_activity(activity: UserActivity):
    print(f"User activity logged: {activity}")
    return {"status": "success"}

class Paper(BaseModel):
    title: str
    abstract: str

class PaperList(BaseModel):
    papers: List[Paper]