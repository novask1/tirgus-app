from tools.db_handler import supabase

def test_fields(table_name, fields_dict):
    try:
        response = supabase.table(table_name).insert(fields_dict, returning="representation").execute()
        print(f"✅ Éxito con campos: {list(fields_dict.keys())}")
        print(f"Resultado: {response.data}")
        return True
    except Exception as e:
        print(f"❌ Error con campos {list(fields_dict.keys())}: {e}")
        return False

def main():
    table_name = "listings"  # Cambia esto si es diferente

    # Probar diferentes combinaciones de campos comunes
    test_combinations = [
        {"title": "Test", "price": 10.0},
        {"name": "Test", "price": 10.0},
        {"title": "Test", "description": "Test desc", "price": 10.0},
        {"id": "test-123", "title": "Test", "price": 10.0},
        {"user_id": "test-123", "title": "Test", "price": 10.0},
        {"seller_id": "test-123", "title": "Test", "price": 10.0},
    ]

    print(f"Probando inserciones en tabla '{table_name}':")
    for fields in test_combinations:
        test_fields(table_name, fields)

if __name__ == "__main__":
    main()