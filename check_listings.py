from tools.db_handler import supabase

def main():
    try:
        # Intentar insertar con un campo dummy para ver qué campos existen
        test_data = {"test_field": "test_value"}
        response = supabase.table("listings").insert(test_data, returning="representation").execute()
        print("Inserción de prueba exitosa:")
        print(response.data)
    except Exception as e:
        print(f"Error con inserción de prueba: {e}")

if __name__ == "__main__":
    main()