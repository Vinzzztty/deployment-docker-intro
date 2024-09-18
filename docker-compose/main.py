from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

client = MongoClient("mongodb://mongodb:27017")
db = client["myDatabase"]
collection = db["users"]


class User(BaseModel):
    name: str
    email: str


@app.post("/user/", response_model=User)
def create_user(user: User):
    user_id = collection.insert_one(user.dict()).inserted_id

    return user, user_id


@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: str):
    user = collection.find_one({"_id": ObjectId(user_id)})
    return user


@app.get("/users/", response_model=List[User])
def list_users():
    users = list(collection.find())

    return users


@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})

    return collection.find_one({"_id": ObjectId(user_id)})


@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": f"User {user_id} deleted"}
