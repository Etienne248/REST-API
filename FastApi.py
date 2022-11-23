from fastapi import FastAPI
import datetime
import json

app = FastAPI(name="Test")

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Todo:
    def __init__(self, ID : int,Title : str, State : int, Due_date : str , Description : str ):
        self.ID=ID
        self.Title=Title
        self.State= State  #(0 : todo, 1 : done)
        self.Due_date = Due_date
        self.Description= Description

todoList = []

@app.get("/todo")
async def get_Todo():
    return {"todoList" : json.dumps(todoList)}  

@app.post("/todo")
async def create_Todo(todo = Todo):
    newtodo = Todo()
    todoList.append(newtodo)
    return {"message": "post created"}