"""
Exercise: Parameters and Input in FastAPI

Write a simple script that creates a FastAPI app and defines a POST method that takes one path parameter, 
one query parameter, and a request body containing a single field. Have this function return all three in a dict. 
To get started, you can use the following snippet -- note the missing imports:
"""

from fastapi import FastAPI
from pydantic import BaseModel
import logging

# Instantiate the app.
app = FastAPI()
logger = logging.getLogger("uvicorn.info")

logger.info("HELLO")

class Value(BaseModel):
  value: int

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello()-> str:
    return {"greeting": "Hello World!"}

@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value)-> dict:
  return {"path": path, "query": query, "body": body}