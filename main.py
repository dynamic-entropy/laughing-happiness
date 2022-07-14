from typing import Union
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"Hello World!"}

@app.get("/api/{endpoint}")
def api(endpoint: Union[str, None] = None):
    return {"healthy": 1, "endpoint":endpoint}