from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/python2")
def hello_world():
    return {"message": "Hello World 2"}
