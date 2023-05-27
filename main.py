from fastapi import FastAPI
from db import Base, engine
from routers import image_router, authentication_router, application_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='reuse')

app.mount('/uploads', StaticFiles(directory='uploads'), name='uploads')

Base.metadata.create_all(engine)

app.include_router(image_router, tags=['Image'])
app.include_router(authentication_router, tags=['Authentication'])
app.include_router(application_router, tags=['Application'])