
from pydantic import BaseModel, Field
from typing import Any, Optional
class ItemBase(BaseModel):
    name: str = Field(..., max_length=100, description="The name of the item")
    description: str | None = Field(None, description="A description of the item")
    price: float = Field(..., gt=0, description="The price of the item, must be a positive number")

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: str | None = Field(None, max_length=100, description="The name of the item")
    description: str | None = Field(None, description="A description of the item")
    price: float | None = Field(None, gt=0, description="The price of the item, must be a positive number")



class Item(ItemBase):
    id: int = Field(..., description="The unique identifier of the item")

    class Config:
        orm_mode = True


class ResponseBase(BaseModel):
    status: str
    message: str
    data: Optional[Item] = None