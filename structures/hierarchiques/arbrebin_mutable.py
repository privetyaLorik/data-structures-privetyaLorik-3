from typing import TypeVar, Generic

T = TypeVar('T')  # Type générique

class ArbreBin(Generic[T]):
    def __init__(self, val: T, gauche: 'ArbreBin[T] | None' = None, droite: 'ArbreBin[T] | None' = None):
        self.data = val
        self.gauche = gauche
        self.droite = droite

    def est_feuille(self):
        return self.gauche is None and self.droite is None

# Remplacez 'ab.ArbreBin' par 'ArbreBin' dans le reste du script.
