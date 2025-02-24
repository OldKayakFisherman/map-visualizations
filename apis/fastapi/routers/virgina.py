from fastapi import APIRouter

router = APIRouter(prefix="/virginia", tags=["virginia"])


@router.get("/landmarks/", tags=["landmarks"])
async def landmarks():
    return [{"username": "Rick"}, {"username": "Morty"}]


