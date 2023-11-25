from fastapi import APIRouter

router = APIRouter()


@router.get('/',  summary='Заглушка',)
async def read_root():
    return {'Hello': 'FastAPI'}
