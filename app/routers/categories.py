from fastapi import APIRouter, Depends, status
from app.dependencies import get_db_connection
from app.models import category
from app import schema
# from ..config import settings

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    dependencies=[Depends(get_db_connection)]
)


@router.get("/")
async def get_categories(session = Depends(get_db_connection)):
    return session.query(schema.Category)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_categories(category: category.CategoryCreate, session = Depends(get_db_connection) ):
    db_category = schema.Category(name = category.name)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category

@router.put("/{category_id}")
async def add_categories(category_id: int, name:str, session = Depends(get_db_connection)):
    db_category = schema.Category(name=name, id=category_id)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category