from pydantic import BaseModel

class categorySchema(BaseModel):
    name: str
    
    
class productSchema(BaseModel):
    name: str
    category_id: int


class aboutSchema(BaseModel):
    description: str
    
    
class loginSchema(BaseModel):
    email: str
    password: str
    
    
class registerSchema(BaseModel):
    username: str
    email: str
    password: str

