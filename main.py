from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def main():
    return {"hello":"hello world"}

uvicorn.run(app=app,host="127.0.0.1",port=8000)