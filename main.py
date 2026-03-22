from fastapi import FastAPI
from routes.generate import router

app = FastAPI()

app.include_router(router)