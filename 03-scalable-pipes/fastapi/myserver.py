"""
Exercise: Parameters and Input in FastAPI

Write a simple script that creates a FastAPI app and defines a POST method that takes one path parameter, 
one query parameter, and a request body containing a single field. Have this function return all three in a dict. 
To get started, you can use the following snippet -- note the missing imports:
"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import json
import pickle
import logging

# Instantiate the app.
app = FastAPI()

logger = logging.getLogger("uvicorn.info")
logger.info("model_server: app is up!")

logger.info("model_server: Loading model.")
try:
    model = pickle.load(open("iris_rfc.pkl", "rb"))
    logger.info(f'model_server: Iris model loaded.')
except Exception as e:
    logger.info(f'model_server: Load model failed!!!')
    model = None

class Value(BaseModel):
  value: int

class Iris(BaseModel):
    sepal_length: float = 5.4
    sepal_width: float = 3
    pedal_length: float = 3.75
    pedal_width: float = 1.1
    

@app.get("/")
async def say_hello()-> str:
    logger.info("model_server: say_hello() GET")
    return {"greeting": "Hello World!"}


@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value)-> dict:
  logger.info(f"model_server: exercise_function() POST: path={path} query={query} body={body}")
  return {"path": path, "query": query, "body": body}


@app.post("/predict/")
async def make_prediction(body: Iris)-> dict:
  global model
  logger.info(f"model_server: make_prediction() POST: body={body}")
  predict_request = np.array([body.sepal_length, body.sepal_width, body.pedal_length, body.pedal_width]).reshape(1,-1)
  ret = model.predict(predict_request)
  # Convert to an int.
  serialized = ret.tolist()[0]
  logger.info(f"model_server: prediction = {serialized}")
  return {"Prediction": serialized}