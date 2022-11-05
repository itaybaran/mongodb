from fastapi import FastAPI
from pymongo_get_database import get_database
from pymongo import MongoClient


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    db = get_database()
    collection = db["user_1_items"]
    item = collection.find_one({"_id": item_id})
    return {"item_id": item_id}