from fastapi import Depends, FastAPI, Header, HTTPException
from routers import router
from dotenv import load_dotenv
from pydantic import BaseModel
from arq import create_pool
load_dotenv()

app = FastAPI()

async def verifier_api_key(x_api_key: str = Header()):
    if x_api_key == "sniper-2026":
        return x_api_key
    else:
        raise HTTPException(status_code=403, detail="Clé API invalide")

@app.get("/health/")
async def health_check(_ = Depends(verifier_api_key)):
    return {"status": "ok"}
app.include_router(router)


