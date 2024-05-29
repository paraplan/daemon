from datetime import date

from fastapi import FastAPI

from src.bridge import main

app = FastAPI()


@app.get("/")
async def root(date: date):
    return await main(date)
