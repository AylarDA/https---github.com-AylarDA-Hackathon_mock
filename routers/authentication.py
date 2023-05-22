from fastapi import *
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import *
from sqlalchemy.orm import *
from models import registerSchema, loginSchema
from db import get_db
import crud


authentication_router = APIRouter()

@authentication_router.post('/signUp')
def signUp(req: registerSchema, db: Session = Depends(get_db)):
    try:
        result = crud.signUp(req, db)
        if result == -1:
            return JSONResponse(status_code=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, content={'result': 'Failed to sign up'})
        elif result:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'Succesfully signed up'})    
        else:
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={'result': 'Failed to sign up'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')


@authentication_router.post('/signIn')
def signIn(req: loginSchema, db: Session = Depends(get_db)):
    try:
        result = crud.signIn(req, db)
        if result:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'Succesfully signed in'})
        else:
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={'result': 'Failed to sign in'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')
    

@authentication_router.get('/users')
def get_users(db: Session = Depends(get_db)):
    try:
        result = crud.read_users(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')

