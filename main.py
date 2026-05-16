from fastapi import Depends, FastAPI, Header, HTTPException
from routers import router
from dotenv import load_dotenv
from pydantic import BaseModel
import sentry_sdk
import os
from arq import create_pool
load_dotenv()

app = FastAPI()
import sentry_sdk

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    traces_sample_rate=0.1,
    send_default_pii=False  
)
async def verifier_api_key(x_api_key: str = Header()):
    if x_api_key == "sniper-2026":
        return x_api_key
    else:
        raise HTTPException(status_code=403, detail="Clé API invalide")

@app.get("/health/")
async def health_check(_ = Depends(verifier_api_key)):
    return {"status": "ok"}
app.include_router(router)


