from fastapi import status, APIRouter
import logging


logger = logging.getLogger()

router = APIRouter(
    prefix="/elevator",
    tags=['Elevator']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def HelloWorld():
    try:
        return 'hello world!'
    except Exception as ex:
        logger.error(ex)