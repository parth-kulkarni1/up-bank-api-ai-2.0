from typing import Any

from fastapi import APIRouter, Depends
from fastapi import HTTPException, Response

from upbankapi.models.transactions import AsyncTransaction
from upbankapi.exceptions import UpBankException

from services.up_bank_service import UpBankAPI

async def get_upbank_service() -> UpBankAPI: 
    return UpBankAPI()

router = APIRouter()

@router.get("/ping")
async def ping(up_bank_api_service: UpBankAPI = Depends(get_upbank_service)) -> Response: 
    try: 
        response = await up_bank_api_service.health_check()

        return Response(
            content=response, 
            status_code=200
        )

    except UpBankException as error: 
        raise HTTPException(
            detail={"Error": error.detail},
            status_code= int(error.status)
        )

@router.get("/transactions")
async def get_transactions(
    account: str, 

) -> Any:
    pass

