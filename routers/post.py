from fastapi import APIRouter, Depends, UploadFile, File
from routers.schemas import ItemBase, ItemDisplay
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_post
import string
import random
import shutil

router = APIRouter(prefix='/post', tags=['post'])

@router.post('')
def create(request: ItemBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)

@router.get('/all')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_post.delete_id(id, db)

@router.delete('/delete/all')
def delete_all(db: Session = Depends(get_db)):
    return db_post.delete_all(db)

@router.post('/{id}/update')
def udpate(id: int, request: ItemBase, db: Session = Depends(get_db)):
    return db_post.update_id(id, request, db)
