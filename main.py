from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from bcrypt import checkpw
from datetime import date

app = FastAPI()

valid_users = dict()
pending_users = dict()
class User(BaseModel):
    username: str
    password: str


class UserType(str, Enum):
    admin = 'admin'
    teacher = 'teacher'
    student = 'student'
    alumni = 'alumni'


class UserProfile(BaseModel):
    first_name: str
    last_name: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date
    user_type: UserType


@app.get("/api/index")
def index():
    return {'message': 'Welcome to FastApi'}


@app.get("/api/login")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return {'message': 'User doesnt exist'}
    else:
        user: valid_users.get(username)
        if checkpw(password.encode(), user.passphare.encode()):
            return user
        else:
            return {'message': 'Invalid user'}


@app.post("/api/login/signup")
def signup(username: str, password: str):
    if username == None or password == None:
        return {'message': 'Invalid user'}
    elif not valid_users.get(username) == None:
        return {'message': 'User exist'}
    else:
        user = User(username=username, password=password)
        pending_users[username] = user
        return user
