from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Word"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}
