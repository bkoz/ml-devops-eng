"""
File: apitesting.py
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
import logging

app = FastAPI()

logger = logging.getLogger("uvicorn.info")

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    logger.info("get_items()")
    return {"fetch": f"Fetched {count} of {item_id}"}