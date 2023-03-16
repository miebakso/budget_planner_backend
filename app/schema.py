from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# This files contain all the database schema

class Category(Base):
    '''
    This class represent the category of spending / transcation
    Ex: Utility / Rent / Health
    '''
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    transactions = relationship("Transaction")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    description = Column(String(50))
    date = Column(DateTime)
    total = Column(Float)
    notes = Column(String(200), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", lazy="joined")
    
    

    

