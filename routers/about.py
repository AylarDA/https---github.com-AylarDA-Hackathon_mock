from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models import aboutSchema
from db import get_db
import crud


about_router = APIRouter()

@about_router.post('/add-about')
def add_about(req: aboutSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_about(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    
    
@about_router.get('/get-about')
def get_about(db: Session = Depends(get_db)):
    try:
        result = crud.read_about(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
