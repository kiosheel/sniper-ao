from pydantic import BaseModel
from fastapi import APIRouter
from arq import create_pool
router = APIRouter()

class Analyse(BaseModel):
    mon_fichier: str
    nb_pages: int
@router.post("/analyses")
async def health_check(body: Analyse):
    return {"message": f"Analyse de {body.mon_fichier} lancée", "pages": body.nb_pages}

@router.post("/analyses/lancer/{fichier_id}")
async def upload_dce(fichier_id: int):
    redis = await create_pool()
    await redis.enqueue_job("analyser_dce", fichier_id=fichier_id)
    return {"message": "Analyse en cours, revenez dans quelques instants"}

