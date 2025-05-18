from fastapi import FastAPI

app = FastAPI(title="API Chatbot", description="Chatbot API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Hello World"}
