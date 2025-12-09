import json
from fastapi import FastAPI
from models.main_models import Item, ItemList, RestrictedItem


app = FastAPI()


@app.post("/items")
async def get_item(item: Item):
    """Get an Item object as Json"""
    return {
        "item_id": item.item_id,
        "product_name": item.prod_name,
        "is_available": item.is_available,
    }


@app.post("/items/restricted")
async def get_item_with_restrictions(item: RestrictedItem):
    """Get an Item object with restrictions as Json"""
    return {
        "item_id": item.item_id,
        "product_name": item.prod_name,
        "is_available": item.is_available,
    }


@app.post("/items/item_list")
async def get_item_list_with_restriction(items: ItemList):
    """Get a list of restricted items in Json format"""
    item_list = []
    if items:
        for s_item in items.item_list:
            item_list.append({
                "item_id": s_item.item_id,
                "product_name": s_item.prod_name,
                "is_available": s_item.is_available
            })
    return json.dumps(item_list)
