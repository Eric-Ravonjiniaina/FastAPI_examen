import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse


app = FastAPI()

Objects = []

class Object(BaseModel):
    Reference = str
    author: str
    title: str
    content: str
    creation_datetime: datetime

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

@app.get("/ping")
def ping():
    return Response(content="pong", status_code=200)

@app.get("/home")
def welcome():
    with open("welcome.html", "r", encoding="utf-8") as file:
        html_content = file.read()
        return Response(content=html_content, status_code=200, media_type="text/html")

@app.get("/{full_path:path}")
async def catch_all():
    with open("not_found.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    return Response(content=html_content, status_code=404, media_type="text/html")

@app.post("/posts")
def add_Object(new_Object: List[Object]):
    global Objects
    Objects.extend(new_Object)
    return JSONResponse(content=[Objet.dict() for Objet in Objects], status_code=201)

@app.get("/posts")
def get_Objects():
    return JSONResponse(content=[Objet.dict() for Objet in Objects], status_code=200)

@app.put("/posts")
def update(title):
    global Objects

    for i, existing_title in enumerate(Objects):
        if existing_title.Reference == Object.Reference:
            Objects[i] = Object
            return JSONResponse(content=title.dict(), status_code=200)

    Objects.append(Object)
    return JSONResponse(content=title.dict(), status_code=200)
