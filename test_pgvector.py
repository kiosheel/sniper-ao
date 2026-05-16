import os
from mistralai.client import Mistral
from dotenv import load_dotenv
from database import supabase
load_dotenv()
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

chunks = [
    "Le titulaire sera pénalisé de 1/3000ème du montant du marché par jour de retard.",
    "Les travaux devront être achevés dans un délai de 90 jours à compter de l'ordre de service.",
    "Le maître d'ouvrage se réserve le droit de résilier le marché en cas de manquement grave."
]
chunks_embedding = client.embeddings.create(
    model="mistral-embed",
    inputs=chunks
)
chunks_vecteurs = [(chunks[i], chunks_embedding.data[i].embedding) for i in range(len(chunks))]
for texte, vecteur in chunks_vecteurs:
    supabase.table("chunks").insert({
        "contenu": texte,
        "embedding": vecteur,
        "analyse_id": 4
    }).execute()

question = "Quelle est la pénalité financière en cas de retard ?"
question_reponse = client.embeddings.create(
    model="mistral-embed",
    inputs=[question]
)
question_vecteur = question_reponse.data[0].embedding
resultat = supabase.rpc(
    "match_chunks",
    {
        "query_embedding": question_vecteur,
        "match_count": 3 
    }
).execute()

chunks_pertinents = resultat.data
prompt = f"""Tu es un expert juridique et financier des marchés publics et du BTP en France.

En te basant UNIQUEMENT sur les extraits du DCE ci-dessous, réponds à la question suivante :
"{question}"

Extraits du DCE :
{chunks_pertinents}

Règles :
- Utilise UNIQUEMENT les informations présentes dans les extraits
- Si l'information n'est pas dans les extraits, dis-le clairement
- Ne jamais inventer de montants ou de délais
- Cite toujours le passage exact sur lequel tu te bases

Structure ta réponse ainsi :
1. Réponse directe à la question
2. Détail et explication
3. Source (extrait exact du DCE)
"""
reponse = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": prompt}]
)
print(reponse.choices[0].message.content)