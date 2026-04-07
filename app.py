from fastapi import FastAPI, Request, HTTPException
from utils.sql_utils import *
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 6969))

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

@app.post("/folders", status_code=201)
async def create_folder_api(request: Request):
    body = await request.json()
    name = body.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="name is required")
    description = body.get("description")
    create_folder(name, description)
    return {"message": "folder created"}

@app.get("/folders")
def get_folders_api():
    return get_folders()

@app.post("/notes", status_code=201)
async def create_note_api(request: Request):
    body = await request.json()
    folder_id = body.get("folder_id")
    title = body.get("title")
    content = body.get("content")
    if not folder_id:
        raise HTTPException(status_code=400, detail="folder_id is required")
    create_note(folder_id, title, content)
    return {"message": "note created"}

@app.get("/notes")
def get_notes_api():
    return get_notes()

@app.get("/notes/{folder_id}")
def get_notes_folder_api(folder_id: int):
    return get_notes_by_folder(folder_id)

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=HOST,
        port=PORT,
        reload=False
    )