from fastapi import APIRouter, Depends, status, HTTPException
from app.dependencies import get_db_connection
from app.models.category import CategoryCreate, CategoryUpdate
from app.schema import Category
import sqlalchemy
# from ..config import settings

router = APIRouter(
    prefix="/categories",
    tags=["categories"],

)

# Return all the categories order by their ID
@router.get("/")
async def get_categories(session = Depends(get_db_connection)):
    return session.query(Category).order_by(Category.id.asc()).all()

# Return a specific category by their ID
@router.get("/{category_id}")
async def get_category(category_id: int, session = Depends(get_db_connection)):
    return session.query(Category).filter(Category.id == category_id).first()

# Create new category, all category is converted to lower case.
@router.post("/")
async def add_categories(category: CategoryCreate, session = Depends(get_db_connection)):
    db_category = Category(name = category.name.lower())
    # Handle duplicate values
    try:
        session.add(db_category)
        session.commit()
        session.refresh(db_category)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=422, detail="Duplicated found, category has existed.")
    return db_category

# Update a category by their ID
@router.put("/{category_id}")
async def update_category(category_id:int, category: CategoryUpdate, session = Depends(get_db_connection)):
    db_category =session.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category Not Found")
    db_category.name = category.name.lower()
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category

# Removed a category by their ID
@router.delete("/{category_id}")
async def remove_category(category_id:int, session = Depends(get_db_connection)):
    db_category = session.query(Category).filter(Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Category Not Found")
    session.delete(db_category)
    session.commit()
    return {'msg':'Category has been deleted'}