from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models import categorySchema
from db import get_db
import crud


category_router = APIRouter()

@category_router.post('/add-category')
def add_category(req: categorySchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_category(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    

@category_router.get('/get-category')
def get_category(db: Session = Depends(get_db)):
    try:
        result = crud.read_category(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')


@category_router.get('/get-current-category-with-path/{id}')
def get_category(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.read_current_category(id, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    
    

