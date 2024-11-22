from fastapi import FastAPI

from settings import UserData
from main import chat_response_generator

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
async def chat(user_data: UserData):
  return chat_response_generator(type=user_data.type, category=user_data.category, query=user_data.query, data=user_data.data)
