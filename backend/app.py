# app.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from indexer import CDPIndexer

app = FastAPI()

# Enable CORS so the React frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins (adjust for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize our doc indexer
indexer = CDPIndexer()

# In-memory feedback store (for demo). In production, use a DB.
feedback_store = []

@app.get("/")
def read_root():
    return {"message": "CDP Chatbot Backend is running!"}


@app.post("/query")
async def handle_query(request: Request):
    """
    Main endpoint for user queries.
    Incorporates:
      1) Irrelevant question check
      2) Cross-CDP comparison
      3) Basic/Advanced 'how-to' fallback
    """
    data = await request.json()
    user_query = data.get("question", "").lower().strip()

    # STEP 1: IRRELEVANT QUESTIONS
    cdp_keywords = ["segment", "mparticle", "lytics", "zeotap"]
    if not any(keyword in user_query for keyword in cdp_keywords):
        return JSONResponse(content={
            "answer": "I can only answer questions related to Segment, mParticle, Lytics, or Zeotap."
        })

    # STEP 2: CROSS-CDP COMPARISONS
    if "compare" in user_query or "difference" in user_query or "vs" in user_query:
        return handle_comparison(user_query)

    # STEP 3: BASIC & ADVANCED 'HOW-TO'
    # Using the same search function, advanced questions are covered if the docs contain advanced info.
    results = indexer.search(user_query)
    if not results:
        return JSONResponse(content={
            "answer": "I couldn't find a direct answer. Please check the official documentation or try rephrasing your query."
        })

    # Format the top results into a single answer
    answer_snippets = []
    for r in results:
        platform = r["platform"]
        snippet = r["content"][:300]
        url = r.get("url", "No URL provided")
        answer_snippets.append(
            f"\n---\n[Source: {platform}]\nSnippet: {snippet}...\nURL: {url}"
        )

    final_answer = "\n".join(answer_snippets)

    return JSONResponse(content={"answer": final_answer})


@app.post("/feedback")
async def handle_feedback(request: Request):
    """
    Allows users to submit feedback on answers.
    Example request body:
      {
        "question": "How do I set up Segment?",
        "rating": 4,  # or 'useful', 'not useful', etc.
        "comment": "Great answer!"
      }
    """
    data = await request.json()
    question = data.get("question", "")
    rating = data.get("rating", None)
    comment = data.get("comment", "")

    feedback_entry = {
        "question": question,
        "rating": rating,
        "comment": comment
    }
    feedback_store.append(feedback_entry)

    return JSONResponse(content={
        "message": "Thanks for your feedback!",
        "submittedFeedback": feedback_entry
    })


def handle_comparison(query: str):
    """
    Detect which CDPs are mentioned in the query.
    Return a structured comparison snippet from the docs.
    """
    platforms = []
    if "segment" in query:
        platforms.append("Segment")
    if "mparticle" in query:
        platforms.append("mParticle")
    if "lytics" in query:
        platforms.append("Lytics")
    if "zeotap" in query:
        platforms.append("Zeotap")

    if len(platforms) < 2:
        return JSONResponse(content={
            "answer": "Please specify at least two platforms to compare (e.g., Segment vs Lytics)."
        })

    comparison_results = []
    for platform in platforms:
        docs = [doc for doc in indexer.docs if doc["platform"].lower() == platform.lower()]
        if docs:
            snippet = docs[0]["content"][:200]
            comparison_results.append(f"[{platform}]: {snippet}...")
        else:
            comparison_results.append(f"[{platform}]: No data found for comparison.")

    comparison_output = "\n\n".join(comparison_results)
    return JSONResponse(content={
        "answer": f"Here is a comparison between {', '.join(platforms)}:\n\n{comparison_output}"
    })
