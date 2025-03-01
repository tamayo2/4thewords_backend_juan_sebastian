from sqlmodel import create_engine
from app.config import settings

def test_db_connection():
    try:
        engine = create_engine(settings.DATABASE_URL)
        with engine.connect() as connection:
            print("✅ Conexión exitosa a la base de datos")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    test_db_connection()
