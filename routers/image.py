from fastapi import APIRouter, Depends, status, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from db import get_db
import crud


image_router = APIRouter()

@image_router.post('/upload-img')
def upload_img(id: int, db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_image(id, file, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')


@image_router.get('/get-image')
def get_image(db: Session = Depends(get_db)):
    try:
        result = crud.read_image(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')


@image_router.delete('/delete-img')
def delete_img(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_image(id, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"result":'DELETED'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'NOT'})
