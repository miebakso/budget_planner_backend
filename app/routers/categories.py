from fastapi import APIRouter, Depends
# from ..config import settings

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    # dependencies=[Depends()]
)


@router.get("/")
async def get_categories():
    # return settings.TEST
    return "asd"

@router.post("/")
async def add_categories():
    return "test2"

@router.put("/{category_id}")
async def add_categories(category_id: int, name):
    return "test3"