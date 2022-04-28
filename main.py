from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import  datetime
from uuid import uuid4 as uuid

app = FastAPI()

posts = []

class Post(BaseModel):
    id:Optional[str]
    title:str
    author:str
    content:Text
    create_date:datetime = datetime.now()
    published_at:Optional[datetime]
    published:bool = False

@app.get('/')
def read_root():
    return {"welcome":"welcome to my REST API"}


@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{id}')
def get_post(id:str):
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(404, detail="post not found")

@app.delete('/posts/{id}')
def delete_post(id:str):
    for index, post in enumerate(posts):
        if post["id"] == id:
            posts.pop(index)
            return {"message" : "post deleted"}
    raise HTTPException(404, detail="post not found")

@app.put('/posts/{id}')
def update_post(id:str, updatePost: Post):
    for index, post in enumerate(posts):
        if post["id"] == id:
            posts[index]["title"] = updatePost.title
            posts[index]["content"] = updatePost.content
            posts[index]["author"] = updatePost.author
            return {"message": "post has been updated suc"}
    raise HTTPException(404, detail="post not found")

