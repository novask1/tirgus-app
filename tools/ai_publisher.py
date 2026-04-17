"""
AI Publisher - Automatic Product Listing from Images

This script analyzes product images and automatically creates listings in the Supabase database.

Usage:
    python tools/ai_publisher.py <image_path>

Features:
- Automatic image analysis (currently filename-based, AI vision planned)
- Generates compelling titles, descriptions, categories, and prices
- Integrates with Supabase database via db_handler.py
- Supports various product categories

Future enhancements:
- Real AI vision analysis using OpenAI Vision API or similar
- Image upload to cloud storage
- Batch processing of multiple images
- User authentication and profile management
"""


def analyze_image(image_path: str) -> Tuple[str, str, str, float]:
    """
    Analyze an image and return suggested title, description, category, and price.

    Args:
        image_path: Path to the local image file

    Returns:
        Tuple of (title, description, category, price)
    """
    # TODO: Implement actual AI vision analysis
    # For now, use filename-based heuristics and placeholder for real vision

    image_name = Path(image_path).stem.lower()

    # Basic keyword matching for common items
    if any(keyword in image_name for keyword in ["camiseta", "shirt", "tshirt", "remera"]):
        return (
            "Camiseta de Algodón Premium",
            "Camiseta cómoda y elegante, perfecta para uso diario. Excelente calidad y diseño moderno.",
            "ropa",
            29.99
        )
    elif any(keyword in image_name for keyword in ["telefono", "phone", "celular", "mobile"]):
        return (
            "Smartphone Android",
            "Teléfono inteligente en perfectas condiciones con todas las funciones. Incluye accesorios.",
            "electronica",
            199.99
        )
    elif any(keyword in image_name for keyword in ["libro", "book", "novela"]):
        return (
            "Libro Coleccionable",
            "Libro en excelente estado, ideal para lectores apasionados. Contenido fascinante.",
            "libros",
            15.50
        )
    elif any(keyword in image_name for keyword in ["bicicleta", "bike", "bici"]):
        return (
            "Bicicleta de Montaña",
            "Bicicleta resistente y confiable para aventuras al aire libre. En perfectas condiciones.",
            "deportes",
            299.99
        )
    elif any(keyword in image_name for keyword in ["guitarra", "guitar"]):
        return (
            "Guitarra Acústica",
            "Instrumento musical de calidad con un sonido excepcional. Perfecto para músicos.",
            "musica",
            149.99
        )
    else:
        # Generic fallback
        return (
            f"Producto Único: {image_name.replace('_', ' ').title()}",
            f"Producto de alta calidad analizado automáticamente. Descubre este artículo especial con características únicas.",
            "general",
            25.00
        )


def publish_item_from_image(image_path: str, user_id: str = None) -> dict:
    """
    Analyze an image and automatically publish it to the database.

    Args:
        image_path: Path to the local image file
        user_id: User ID for the listing (defaults to None)

    Returns:
        The inserted item data
    """
    # Validate image exists
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Analyze the image
    title, description, category, price = analyze_image(image_path)

    # Insert into database
    item = insert_item(
        seller_id=user_id,
        title=title,
        description=description,
        price=price,
        category=category,
        media_urls=[],  # Could be extended to upload image to cloud storage
        location_name=None,
        lat=None,
        lng=None,
    )

    return item


def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/ai_publisher.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    try:
        # Use None for user_id since the UUID doesn't exist in profiles
        user_id = None  # "48565f99-9e2e-4195-b5b8-9b32130a8aab" doesn't exist in profiles table

        print(f"Analizando imagen: {image_path}")
        item = publish_item_from_image(image_path, user_id)

        print("✅ Producto publicado exitosamente!")
        print(f"ID: {item['id']}")
        print(f"Título: {item['title']}")
        print(f"Descripción: {item['description']}")
        print(f"Precio: ${item['price']}")
        print(f"Categoría: {item.get('category', 'N/A')}")
        print(f"Fecha: {item['created_at']}")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()