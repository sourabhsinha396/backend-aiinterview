from fastapi import FastAPI
from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME, description=settings.PROJECT_DESCRIPTION, version=settings.PROJECT_VERSION)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
