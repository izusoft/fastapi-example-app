from fastapi import APIRouter

from api.routes import example

router = APIRouter()
# example router
router.include_router(example.router, tags=["example"], prefix="/items")
