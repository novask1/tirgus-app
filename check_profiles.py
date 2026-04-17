from tools.db_handler import supabase

def main():
    try:
        # Consultar usuarios existentes en profiles
        response = supabase.table("profiles").select("id").limit(5).execute()
        print("Usuarios disponibles en profiles:")
        for profile in response.data:
            print(f"  - {profile['id']}")
        if not response.data:
            print("  No hay usuarios en profiles")
    except Exception as e:
        print(f"Error al consultar profiles: {e}")

if __name__ == "__main__":
    main()