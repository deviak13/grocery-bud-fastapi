from fastapi import HTTPException, status
from routers.schemas import ItemBase
from sqlalchemy.orm.session import Session
from database.models import DbItem
import datetime

def create(db: Session, request: ItemBase):
    new_item = DbItem(
        title = request.title,
        timestamp = datetime.datetime.now()
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def get_all(db: Session):
    return db.query(DbItem).all()

def delete_id(id: int, db: Session):
    item = db.query(DbItem).filter(DbItem.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Item with id {id} does not exist')
    db.delete(item)
    db.commit()
    return f'Item with id {id} successfully deleted'

def delete_all(db: Session):
    db.query(DbItem).delete()
    db.commit()
    return 'All items deleted'

def update_id(id: int, request: ItemBase, db: Session):
    item = db.query(DbItem).filter(DbItem.id == id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Item with id {id} does not exist')
    item.update({
        DbItem.title: request.title
    })
    db.commit()
    return f'Update of item with id {id} successful'
