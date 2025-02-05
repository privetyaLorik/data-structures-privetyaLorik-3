import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager
from typing import Generator
import dotenv
import os

# Chargement du fichier .env
dotenv.load_dotenv()

# Construction du pool de connexions en fonction des variables d'environnement
# Il ne faut jamais faire figurer d'informations sensibles dans le code.
# Les informations de connexion à la base de données sont externalisées dans un fichier.
POOL = ThreadedConnectionPool(
    minconn=1,
    maxconn=10,
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
    sslmode=os.getenv('DB_SSLMODE')
)

@contextmanager
def get_connection() -> Generator[psycopg2.extensions.connection, None, None]:
    """
    Un gestionnaire de contexte qui fournit une connexion PostgreSQL via
    le pool de connexions ThreadedConnectionPool.

    La connexion est automatiquement rendue au pool lorsque le contexte
    est quitté.

    Exemple d'utilisation :
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM table")
                print(cur.fetchall())
    """
    # Récupération d'une connexion disponible du pool
    conn: psycopg2.extensions.connection = POOL.getconn()
    try:
        yield conn     # Renvoie la connection et attend à cette ligne la fin du contexte (with)
        conn.commit()  # Commit automatique si aucune exception n'est levée
    except Exception as e:
        conn.rollback()  # Rollback en cas d'exception
        raise e
    finally:
        POOL.putconn(conn) # Remise de la connexion au pool dans tous les cas


if __name__ == "__main__":
    # Exemple d'utilisation
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM eleves")
            print(cur.fetchall())
    
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM eleves")
            print(cur.fetchall())

