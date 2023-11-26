from fastapi import APIRouter

from backend.api.endpoints import stub_router

main_router = APIRouter()

main_router.include_router(
    stub_router,
    prefix='',
    tags=['Temporary Stub']
)
