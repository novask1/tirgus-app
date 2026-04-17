from tools.db_handler import supabase

def main():
    try:
        # Intentar listar tablas disponibles
        response = supabase.table("information_schema.tables").select("table_name").eq("table_schema", "public").execute()
        tables = [row["table_name"] for row in response.data]
        print("Tablas disponibles en public:")
        for table in tables:
            print(f"  - {table}")
    except Exception as e:
        print(f"Error al listar tablas: {e}")

if __name__ == "__main__":
    main()