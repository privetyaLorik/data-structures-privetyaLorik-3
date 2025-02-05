import database
from modele import Eleve

def get_all_eleves() -> list[Eleve]:
    """Retourne la liste de tous les élèves"""    
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            # Le select est effectué en fonction de l'ordre des paramètres du modèle 
            cur.execute("SELECT id, nom, prenom, age FROM eleves ORDER BY nom, prenom")
            return [Eleve(row[0], row[1], row[2], row[3]) for row in cur.fetchall()]


def get_eleve(id: int) -> Eleve | None:
    """Retourne l'élève d'ID id, ou None si non trouvé"""
    with database.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nom, prenom, age FROM eleves WHERE id = %s", (id,))
            row = cur.fetchone()
            if row is None:
                return None
            return Eleve(row[0], row[1], row[2], row[3])


def create_eleve(nom: str, prenom: str, age: int) -> int:
    """Crée un nouvel élève et retourne son ID"""
    try:
        with database.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO eleves (nom, prenom, age) VALUES (%s, %s, %s) RETURNING id", (nom, prenom, age))
                # L'id est créé automatiquement, on la retourne et on la récupère
                return cur.fetchone()[0]  # type: ignore
    except Exception as e:
        print(f"Erreur lors de la création de l'élève: {e}")
        return -1  # Retourne un ID invalide en cas d'erreur


def update_eleve(id: int, nom: str, prenom: str, age: int) -> None:
    """Modifie l'élève d'ID id"""
    try:
        with database.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE eleves SET nom = %s, prenom = %s, age = %s WHERE id = %s", (nom, prenom, age, id))
    except Exception as e:
        print(f"Erreur lors de la mise à jour de l'élève avec ID {id}: {e}")


def delete_eleve(id: int) -> None:
    """Supprime l'élève d'ID id"""
    try:
        with database.get_connection() as conn:
            with conn.cursor() as cur:
                # Vérifie si l'élève existe avant de tenter de le supprimer
                cur.execute("SELECT id FROM eleves WHERE id = %s", (id,))
                row = cur.fetchone()
                if row is None:
                    print(f"Aucun élève trouvé avec l'ID {id}.")
                    return
                # Si l'élève existe, on le supprime
                cur.execute("DELETE FROM eleves WHERE id = %s", (id,))
                print(f"L'élève avec l'ID {id} a été supprimé.")
    except Exception as e:
        print(f"Erreur lors de la suppression de l'élève avec ID {id}: {e}")
