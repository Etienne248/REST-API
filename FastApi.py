from fastapi import FastAPI

app = FastAPI(name="Test")

donnees = {"messages":"hello word"}
@app.get("/")
def messages():
    return donnees