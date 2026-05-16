from fastapi import APIRouter
from routers import analyses, projets

router = APIRouter()
router.include_router(analyses.router)
router.include_router(projets.router)