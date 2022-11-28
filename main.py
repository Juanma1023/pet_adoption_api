from fastapi import FastAPI

from app.v1.router.user_router import router as user_router
from app.v1.router.location_router import router as location_router
from app.v1.router.species_router import router as species_router
from app.v1.router.pets_router import router as pets_router
from app.v1.router.request_router import router as request_router

app = FastAPI()

app.include_router(user_router)
app.include_router(location_router)
app.include_router(species_router)
app.include_router(pets_router)
app.include_router(request_router)