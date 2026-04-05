from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from app.utils import extract_pdf_comments

app = FastAPI()

API_KEY = "123456"

@app.post("/extract-comments")
async def extract_comments(
    file: UploadFile = File(...),
    x_api_key: str = Header(...)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    content = await file.read()
    comments = extract_pdf_comments(content)

    return {
        "status": "success",
        "data": comments
    }
