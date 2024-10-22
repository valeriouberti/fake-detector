from fastapi import FastAPI, HTTPException

from src.models.model import Article
from src.service.service import OpenAIService

# Initialize FastAPI app
app = FastAPI()
service = OpenAIService()

# FastAPI endpoint for classification
@app.post("/classify/")
def classify_article_endpoint(article: Article):
    try:
        classification = service.classify_article(article.text)
        return {"classification": classification}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
