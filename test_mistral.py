import os
from mistralai.client import Mistral
from dotenv import load_dotenv
import numpy as np
load_dotenv()
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
import numpy as np

def similarite_cosine(vecteur_a, vecteur_b):
    return np.dot(vecteur_a, vecteur_b) / (
        np.linalg.norm(vecteur_a) * np.linalg.norm(vecteur_b)
    )
chunks = [
    "Le titulaire sera pénalisé de 1/3000ème du montant du marché par jour de retard.",
    "Les travaux devront être achevés dans un délai de 90 jours à compter de l'ordre de service.",
    "Le maître d'ouvrage se réserve le droit de résilier le marché en cas de manquement grave."
]
question = "Quelle est la pénalité financière en cas de retard ?"
chunks_embedding = client.embeddings.create(
    model="mistral-embed",
    inputs=chunks
)
question_reponse = client.embeddings.create(
    model="mistral-embed",
    inputs=[question]
)
question_vecteur = question_reponse.data[0].embedding
chunks_vecteurs = [(chunks[i], chunks_embedding.data[i].embedding) for i in range(len(chunks))]
def trouver_meilleur_chunk(question_vecteur, chunks_vecteurs):
    best_score = -1
    meilleur_chunk = None
    for texte, vecteur in chunks_vecteurs:
        score = similarite_cosine(question_vecteur, vecteur)
        if score > best_score:
            best_score = score
            meilleur_chunk = texte

    return meilleur_chunk

print(trouver_meilleur_chunk(question_vecteur, chunks_vecteurs))   