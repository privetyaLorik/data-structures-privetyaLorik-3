from modele import Eleve

eleves = [
        Eleve(1, 'Dupont', 'Jean',15),
        Eleve(2, 'Durand', 'Pierre',16),
        Eleve(3, 'Dufour', 'Paul',17),
    ]

def get_all_eleves() -> list[Eleve]:
    return eleves

def get_eleve(id: int) -> Eleve:
    return [e for e in eleves if e.id == id][0]

def update_eleve(id: int, nom: str, prenom: str, age: int) -> None:
    e = get_eleve(id)
    e.nom = nom
    e.prenom = prenom
    e.age = age

def delete_eleve(id: int) -> None:
    eleves.remove(get_eleve(id))

def create_eleve(nom: str, prenom: str, age:int) -> int:
    newid: int = max(eleves, key=lambda e: e.id).id + 1
    eleves.append(Eleve(newid, nom, prenom, age))
    return newid