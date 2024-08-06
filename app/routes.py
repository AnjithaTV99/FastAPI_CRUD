from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import app.crud_operations as crud_operations
import app.schema as schema

from app.database import get_db

router = APIRouter()

@router.post("/create",response_model=schema.ResponseBase, status_code=status.HTTP_201_CREATED)
def create_item(item: schema.ItemCreate, db: Session = Depends(get_db)):
    try:
        db_item = crud_operations.create_item(db, item)
        return schema.ResponseBase(
            status="success",
            message="Item created successfully",
            data=db_item
        )
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/get_item_by_id/{id}", response_model=schema.ResponseBase,status_code=status.HTTP_200_OK)
def get_item(id: int, db: Session = Depends(get_db)):
    try:
        db_item = crud_operations.get_item(db, id)
        if db_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not found")
        return schema.ResponseBase(
            status="success",
            message="Item retrieved successfully",
            data=db_item
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/update_item_by_id/{id}", response_model=schema.ResponseBase,status_code=status.HTTP_200_OK)
def update_item(id: int, item: schema.ItemUpdate, db: Session = Depends(get_db)):
    try:
        db_item = crud_operations.update_item(db, id, item)
        if db_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not found")
        return schema.ResponseBase(
            status="success",
            message="Item updated successfully",
            data=db_item
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/delete_itm_by_id/{id}", response_model=schema.ResponseBase,status_code=status.HTTP_200_OK)
def delete_item(id: int, db: Session = Depends(get_db)):
    try:
        db_item = crud_operations.delete_item(db, id)
        if db_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {id} not found")
        return schema.ResponseBase(
            status="success",
            message="Item deleted successfully",
            data=db_item
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/get_items", response_model=List[schema.Item],status_code=status.HTTP_200_OK)
def get_items(db: Session = Depends(get_db)):
    try:
        return crud_operations.get_items(db)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
