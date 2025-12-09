from typing import Union, List
from pydantic import BaseModel, Field, PositiveInt


class Item(BaseModel):
    """Base Item class"""
    item_id: int
    prod_name: str
    is_available: bool


class RestrictedItem(BaseModel):
    """Item with restrictions class"""
    item_id: PositiveInt
    prod_name: str = Field(min_length=3, max_length=30)
    is_available: bool


class ItemList(BaseModel):
    """List of items class"""
    item_list: Union[List[RestrictedItem], None]
