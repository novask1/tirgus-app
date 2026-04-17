from tools.db_handler import insert_item


def main() -> None:
    item = insert_item(
        seller_id=None,  # Usar None para user_id
        title="Camiseta Vintage",
        description="Anuncio de prueba para verificar conexión a la base de datos.",
        price=25.50,
        category="ropa",
        media_urls=[],
        location_name=None,
        lat=None,
        lng=None,
    )
    print("Insertado:", item)


if __name__ == "__main__":
    main()
