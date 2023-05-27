from pydantic import BaseModel
    
    
class loginSchema(BaseModel):
    number: str
    password: str
    
    
class registerSchema(BaseModel):
    name: str
    city: str
    adress: str
    number: str
    password: str
    
    
class applicationSchema(BaseModel):
    name : str
    text : str

