#api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.schemas import QueryRequest, QueryResponse
from main import run_query

app = FastAPI(title="Multi-Agent RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Multi-Agent RAG API Running"}

@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):

    dataset = request.dataset if request.dataset else "business"

    result = run_query(request.query, dataset)

    return result