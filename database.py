import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

_url = os.environ.get("SUPABASE_URL", "")
_key = os.environ.get("SUPABASE_SECRET_KEY", "")

supabase: Client | None = create_client(_url, _key) if _url and _key else None