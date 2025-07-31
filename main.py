from fastapi import FastAPI
from starlette.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bonjour, bienvenue sur mon projet API FastAPI !"}

@app.get("/hello")
def hello():
         with open("hello.html", "r", encoding="utf-8") as file:
             html_content = file.read()
             return Response(content=html_content, status_code=200, media_type="text/html")

@app.get("/welcome")
def welcome(name: str = "Guest"):
    return JSONResponse(content={"message": f"Welcome {name}"}, status_code=200)
