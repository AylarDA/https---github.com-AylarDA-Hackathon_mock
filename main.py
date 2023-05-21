from fastapi import FastAPI
from db import Base, engine
from routers import category_router, product_router, image_router, about_router, authentication_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/uploads', StaticFiles(directory='uploads'), name='uploads')

Base.metadata.create_all(engine)

app.include_router(category_router, tags=['Category'])
app.include_router(product_router, tags=['Product'])
app.include_router(image_router, tags=['Image'])
app.include_router(about_router, tags=['About'])
app.include_router(authentication_router, tags=['Authentication'])