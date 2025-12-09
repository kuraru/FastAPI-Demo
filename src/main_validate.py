from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):  # Type annotation ensures 'item_id' is an integer
    return {"item_id": item_id}


@app.get("/items/qp/")
async def read_more_items(item_id: int, prod_name: str):  # query parameters example
    return {"item_id": item_id, "product_name": prod_name}


@app.get("/items/mixed/{item_id}")
async def read_mixed_items(
    item_id: int, prod_name: str, is_available: bool
):  # query with parameters in a mixed fashion
    return {"item_id": item_id, "product_name": prod_name, "is_available": is_available}
