from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import app.models as models, app.schema as schema
import logging

def create_item(db: Session, item: schema.ItemCreate) -> models.Item:
    try:
        db_item = models.Item(name=item.name, description=item.description, price=item.price)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return schema.Item(id=db_item.id, name=db_item.name, description=db_item.description, price=db_item.price)
        
    except SQLAlchemyError as e:
        raise Exception(f"An error occurred while creating the item: {e}")

def get_item(db: Session, item_id: int) -> models.Item | None:
    try:
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
        return schema.Item(id=db_item.id, name=db_item.name, description=db_item.description, price=db_item.price)
    except SQLAlchemyError as e:
        raise Exception(f"An error occurred while retrieving the item: {e}")

def get_items(db: Session) -> list[models.Item]:
    try:
        return db.query(models.Item).all()  
    except SQLAlchemyError as e:
        raise Exception(f"An error occurred while retrieving items: {e}")

def update_item(db: Session, item_id: int, item: schema.ItemUpdate) -> models.Item | None:
    try:
        
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()

        if db_item is None:
            return None  
        
        
        if item.name is not None and item.name != "":
            db_item.name = item.name
        if item.description is not None and item.description != "":
            db_item.description = item.description
        if item.price is not None and item.price > 0:
            db_item.price = item.price
        
        # print(f"Updated item: Name={db_item.name}, Description={db_item.description}, Price={db_item.price}")
        db.commit()
        db.refresh(db_item)
        return schema.Item(id=db_item.id, name=db_item.name, description=db_item.description, price=db_item.price)

    except SQLAlchemyError as e:
        logging.error(f"An error occurred while updating the item: {e}")
        return None
def delete_item(db: Session, item_id: int) -> models.Item | None:
    try:
        db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
        if db_item is None:
            return None
        db.delete(db_item)
        db.commit()
        return schema.Item(id=db_item.id, name=db_item.name, description=db_item.description, price=db_item.price)

    except SQLAlchemyError as e:
        raise Exception(f"An error occurred while deleting the item: {e}")
