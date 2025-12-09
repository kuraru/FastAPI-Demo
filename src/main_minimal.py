from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """Default get handler"""
    return {"Hello": "World"}
