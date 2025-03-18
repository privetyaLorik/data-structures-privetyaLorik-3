import random

type matrice[T] = list[list[T]]
type chemin = list[int]

def init_pheromones(nb_sommets: int, 
                    tau_initial: float=1.0) -> matrice[float]:
    """Initialise la matrice des phéromones à tau_initial.tau_initial est la contribution en phéromones de chaque arête"""
    return [[tau_initial for _ in range(nb_sommets)] for _ in range(nb_sommets)]

def calculer_visibilite(graphe: matrice[float]) -> matrice[float]:
    """Renvoie la matrice de visibilité. La visibilité de chaque arête est l'inverse de la distance"""
    return [[1/e if e != 0 else 0 for e in ligne] for ligne in graphe]

def get_graphe_exemple() -> matrice[float]:
    return [
        [0, 2, 9, 10],
        [2, 0, 6, 4],
        [9, 6, 0, 8],
        [10, 4, 8, 0]
    ]

def prochain_sommet(pheromones: matrice[float],                     
                    visibilite: matrice[float],                     
                    sommet_courant: int,                     
                    inexplore: list[int],                     
                    alpha: float, beta: float) -> int:
    """Renvoit le prochain sommet au hasard en fonction de l attractivité des chemins.    
    Notre fourmi est quand même plus intelligente qu'une fourmi classique, 
    elle ne va pas aux endroits déjà visités.        
    >>> random.seed(54)    
    >>> g = get_graphe_exemple()    
    >>> n = len(g)    
    >>> prochain_sommet(init_pheromones(n), calculer_visibilite(g), 0, list(range(n)), 1, 2)    
    1
    """

    attractivite = list[float] = []
    for s in inexplore:
        attractivite.append(visibilite[sommet_courant][s]**alpha*pheromones[sommet_courant][s]**beta)
    total_att = sum(attractivite)
    probas = [att/total_att for att in attractivite]
    return random.choices(inexplore,weights=probas)
