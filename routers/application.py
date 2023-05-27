from fastapi import APIRouter, Depends, status, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db import get_db
import crud
from models import applicationSchema
from typing import Optional


application_router = APIRouter()

@application_router.post('/add-application')
def add_application(req: applicationSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_application(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    

@application_router.get('/get-application')
def get_application(status: Optional[bool] = None, db: Session = Depends(get_db)):
    try:
        result = crud.read_application(status, db)
        result = jsonable_encoder(result)
        return JSONResponse(content=result)
    except Exception as e:
        print(e)
        return HTTPException(detail='Something went wrong!!!')



@application_router.get('/get-current-application-with-path/{id}')
def get_application(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.read_current_application(id, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    