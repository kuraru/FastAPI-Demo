from typing import List, Optional
from fastapi import FastAPI, HTTPException, Header, Request
from models.main_models import ItemList, RestrictedItem


MAX_ITEMS = 3
app = FastAPI()
items: List[RestrictedItem] = []


@app.post("/items/header_param")
async def header_param(secret_key: Optional[str] = Header(None)):
    """Access request object"""
    return {"secret_key": secret_key}


@app.post("/items/add_item")
async def add_item(item: RestrictedItem):
    """Add an item to the internal storage"""
    if len(items) < MAX_ITEMS:
        items.append(item)
    else:
        raise HTTPException(400, detail="No more space in storage")


@app.get("/items")
async def get_items() -> ItemList:
    """Get all elements in store as list"""
    return ItemList(item_list=items)
