from fastapi import FastAPI, HTTPException, Query
from typing import List
from models import User, UserUpdate
from database import users_db

app = FastAPI()

@app.post("/users/", status_code=201)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists with this ID")
    users_db[user.id] = user
    return {"message": "User created successfully"}

@app.get("/users/{id}")
def get_user_by_id(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[id]

@app.get("/users/search")
def search_users_by_name(name: str = Query(...)):
    result = [user for user in users_db.values() if name.lower() in user.name.lower()]
    return result

@app.put("/users/{id}")
def update_user(id: int, updated_user: UserUpdate):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    user = users_db[id]
    user.name = updated_user.name
    user.phone_no = updated_user.phone_no
    user.address = updated_user.address
    users_db[id] = user
    return {"message": "User updated successfully"}

@app.delete("/users/{id}")
def delete_user(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[id]
    return {"message": "User deleted successfully"}
