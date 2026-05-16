from fastapi import Depends, Header, HTTPException, APIRouter
import os
from database import supabase
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()
router = APIRouter()

class Projet(BaseModel):
    nom: str
    nb_fichiers: int

@router.post("/projets")
async def new_projet(body: Projet):
    try:
        response = supabase.table("projets").insert({"nom": body.nom, "nb_fichiers": body.nb_fichiers}).execute()
        return response.data
    except Exception as e:
        print(f"ERREUR: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/projets/{projet_id}")
async def delete_projet(projet_id: int):
    supabase.table("projets").delete().eq("id", projet_id).execute()
    return {"status": "ok"}