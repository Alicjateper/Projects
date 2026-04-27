from sqlalchemy import create_engine

# tworzy plik bazy danych test.db
engine = create_engine("sqlite:///test.db")

try:
    with engine.connect() as connection:
        print("Połączenie OK!")
except Exception as e:
    print("Błąd:", e)