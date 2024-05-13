from fastapi import FastAPI, Depends
from app.db import create_db_and_tables
import os

app = FastAPI()



@app.on_event("startup")
async def startup():
    await create_db_and_tables()


@app.on_event("shutdown")
async def shutdown():
    os.remove("test.db")