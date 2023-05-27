from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime
    
    
class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
        
    
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    adress = Column(String, nullable=False)
    number = Column(String, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    
class Application(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    text = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
