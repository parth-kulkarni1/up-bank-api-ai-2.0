from upbankapi import AsyncClient 
from typing import Union
from upbankapi.models.accounts import *
from upbankapi.models.transactions import AsyncTransaction
import os
from config import Settings

settings = Settings() #type:ignore

class UpBankAPI:
    def __init__(self, token: Optional[str] = None) -> None:

        if token: 
            self._client = AsyncClient(token=token)

        self._client = AsyncClient(token=settings.UP_BANK_API_KEY)
    
    async def health_check(self) -> str: 

        return await self._client.ping()
    
    async def get_transactions(
        self,
        account: Union[str, Account],
        status: TransactionStatus, 

    ) -> AsyncPaginatedList[AsyncTransaction]:
        
        return await self._client.transactions(
            account=account,
            status=status
        )
    