#api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.schemas import QueryRequest, QueryResponse
from main import run_query

app = FastAPI(title="Multi-Agent RAG API")

# Allow frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace "*" with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Multi-Agent RAG API Running"}

@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    """
    Receives query & dataset, returns structured RAG response
    """
    result = run_query(request.query, request.dataset)

    # Make sure result contains the expected keys
    return {
        "corrected_query": result.get("corrected_query", request.query),
        "documents": result.get("documents", []),
        "answer": result.get("answer", "No answer generated"),
    }