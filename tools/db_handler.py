import os
from typing import Any, Dict, Iterable, Optional

from dotenv import load_dotenv
from supabase import Client, create_client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL") or os.getenv("VITE_SUPABASE_URL")
SUPABASE_KEY = (
    os.getenv("SUPABASE_KEY")
    or os.getenv("VITE_SUPABASE_ANON_KEY")
    or os.getenv("VITE_SUPABASE_SERVICE_ROLE_KEY")
)

if not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError(
        "Missing SUPABASE_URL or SUPABASE_KEY in .env. "
        "Expected SUPABASE_URL/SUPABASE_KEY or VITE_SUPABASE_URL/VITE_SUPABASE_ANON_KEY."
    )

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_item(
    seller_id: str,
    title: str,
    description: str,
    price: float,
    category: str,
    media_urls: Optional[Iterable[str]] = None,
    location_name: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
) -> Dict[str, Any]:
    """Insert a new product into the items table."""
    payload = {
        "user_id": seller_id,  # Usar seller_id como user_id
        "title": title,
        "description": description,
        "price": price,
        # Los siguientes campos no existen en la tabla listings:
        # "category": category,
        # "media_urls": list(media_urls) if media_urls is not None else [],
        # "location_name": location_name,
        # "lat": lat,
        # "lng": lng,
    }

    response = (
        supabase
        .table("listings")
        .insert(payload, returning="representation")
        .execute()
    )

    # En supabase-py moderno, los errores se lanzan como excepciones
    # No hay response.error, la ejecución exitosa devuelve los datos
    result = response.data
    if not result:
        raise RuntimeError("Item insert succeeded but no data was returned.")

    return result[0]
