from operator import and_
from fastapi import APIRouter, Depends, HTTPException, Body
from app.dependencies import get_db_connection, engine
from app.models.transaction import TransactionCreate, TransactionUpdate, TransationsRequest
from app.schema import Category, Transaction
from sqlalchemy import and_
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import joinedload


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)

# Test functions
@router.get("/")
async def get_transactions(session= Depends(get_db_connection)):
    q = session.query(Transaction).join(Category, Transaction.category_id == Category.id).options(joinedload(Transaction.category))
    # print(str(q.statement.compile(dialect=mysql.dialect())))
    return q.all()

   

# Return all the categories order by their ID
@router.post("/search")
async def search(t_request: TransationsRequest, session= Depends(get_db_connection)):
    query = session.query(Transaction).join(Category, Transaction.category_id == Category.id).options(joinedload(Transaction.category))
    
    # Filter categories if specified
    if t_request.category_ids:
        query = query.filter(Transaction.category_id.in_(tuple(t_request.category_ids)))
    
    # transations order
    order = Transaction.date.asc()
    if not t_request.date_asc :
        order = Transaction.date.desc()
    query = query.order_by(order)

    # filter start date, end date or both
    if t_request.start_date is not None and t_request.end_date is not None:
        query = query.filter(and_(Transaction.date >= t_request.start_date, Transaction.date <= t_request.end_date))
    else: 
        if t_request.start_date is not None:
            query = query.filter(Transaction.date >= t_request.start_date)
        if t_request.end_date is not None:
            query = query.filter(Transaction.date <= t_request.end_date)
    
    # filter offset if specified
    if t_request.page is not None:
        query = query.offset(t_request.page*t_request.page_size - t_request.page_size)
    
    # filter page size if not specified
    if t_request.page_size is not None:
        query = query.limit(t_request.page_size)
    return query.all()

# Return a specific trasantion by their ID
@router.get("/{transcaction_id}")
async def get_transaction_by_id(transcaction_id: int, session = Depends(get_db_connection)):
    return session.query(Transaction).filter(Transaction.id == transcaction_id).join(Category).first()
    
@router.post("/")
async def add_transaction(transaction: TransactionCreate, session = Depends(get_db_connection)):
    db_transactions = Transaction()
    transation_data = transaction.dict()
    for key, value in transation_data.items():
        setattr(db_transactions, key, value)
    # Handle duplicate values
    session.add(db_transactions)
    session.commit()
    session.refresh(db_transactions)
    return db_transactions

# Update a category by their ID
@router.put("/{transaction_id}")
async def update_transaction_by_id(transation_id:int, transaction: TransactionUpdate, session = Depends(get_db_connection)):
    db_transactions = session.query(Transaction).filter(Transaction.id == transation_id).first()
    if not db_transactions:
        raise HTTPException(status_code=404, detail="Transaction Not Found")
    transation_data = transaction.dict()
    for key, value in transation_data.items():
        setattr(db_transactions, key, value)
    session.add(db_transactions)
    session.commit()
    session.refresh(db_transactions)
    return db_transactions

# Removed a category by their ID
@router.delete("/{transaction_id}")
async def remove_transaction(transation_id:int, session = Depends(get_db_connection)):
    db_transaction = session.query(Transaction).filter(Transaction.id == transation_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transation you're trying to removed not found")
    session.delete(db_transaction)
    session.commit()
    return {'msg':'Transation has been deleted'}
