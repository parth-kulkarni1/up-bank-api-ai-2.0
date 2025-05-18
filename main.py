import uvicorn
from fastapi import FastAPI
from routes.api_routes import router as api_router
from typing import Dict

app = FastAPI()

app.include_router(
    router=api_router,
    prefix="/api"
)



@app.get("/")
async def root() -> Dict[str,str]:
    return {"message": "Welcome to this Up Bank Powered AI Assistant"}

if __name__ == "__main__": 
    uvicorn.run(
        app="main:app",
        port=8080, 
        host="localhost",
        reload=True
    )