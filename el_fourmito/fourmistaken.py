###############################################################################################################################
#                                                        Imports                                                              #
###############################################################################################################################

import random
import doctest

###############################################################################################################################
#                                                         Types                                                               #
###############################################################################################################################


type matrice[T] = list[list[T]]
type chemin = list[int]


###############################################################################################################################
#                                               Initialisation_Phéromones                                                     #
###############################################################################################################################


def init_pheromones(nb_sommets: int, 
                    tau_initial: float=1.0) -> matrice[float]:
    """Initialise la matrice des phéromones à tau_initial.tau_initial est la contribution en phéromones de chaque arête"""
    return [[tau_initial for _ in range(nb_sommets)] for _ in range(nb_sommets)]


###############################################################################################################################
#                                                  Calcul_visibilité                                                          #
###############################################################################################################################


def calculer_visibilite(graphe: matrice[float]) -> matrice[float]:
    """Renvoie la matrice de visibilité. La visibilité de chaque arête est l'inverse de la distance"""
    return [[1/e if e != 0 else 0 for e in ligne] for ligne in graphe]


###############################################################################################################################
#                                                  Graphe_d'exemple                                                           #
###############################################################################################################################


def get_graphe_exemple() -> matrice[float]:
    return [
        [0, 2, 9, 10],
        [2, 0, 6, 4],
        [9, 6, 0, 8],
        [10, 4, 8, 0]
    ]


###############################################################################################################################
#                                                    prochain_sommets                                                         #
###############################################################################################################################


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

    attractivite: list[float] = []
    for s in inexplore:
        attractivite.append(visibilite[sommet_courant][s]**beta*pheromones[sommet_courant][s]**alpha)
    total_att = sum(attractivite)
    probas = [att/total_att for att in attractivite]
    return random.choices(inexplore, weights=probas)[0]


###############################################################################################################################
#                                                    Parcours_fourmi                                                          #
###############################################################################################################################


def parcours_fourmi( graphe: matrice[float],                      
                    pheromones: matrice[float],                      
                    visibilite: matrice[float],                      
                    alpha: float, beta: float) -> tuple[chemin, float]:
    """    
    Simule le parcours d'une seule fourmi choisissant au hasard un sommet de départ inexploré.    
    Renvoie le chemin ainsi que la longueur de ce chemin.    
    >>> random.seed(54)    
    >>> g = get_graphe_exemple()    
    >>> n = len(g)    
    >>> parcours_fourmi(g, init_pheromones(n), calculer_visibilite(g), 1, 2)    
    ([1, 0, 2, 3, 1], 23)   
    """
    n = len(graphe)
    sommet_depart = random.randint(0, n-1)
    chemin = [sommet_depart]
    longueur_chemin = 0.0
    
    inexplore = list(range(n))
    inexplore.remove(sommet_depart)
    sommet_courant = sommet_depart
    
    while inexplore:
        prochain = prochain_sommet(pheromones, visibilite, sommet_courant, inexplore, alpha, beta)
        chemin.append(prochain)
        longueur_chemin += graphe[sommet_courant][prochain]
        inexplore.remove(prochain)
        sommet_courant = prochain
    
    chemin.append(sommet_depart)
    longueur_chemin += graphe[sommet_courant][sommet_depart]
    
    return (chemin, int(longueur_chemin))


###############################################################################################################################
#                                                   simuler_colonie                                                           #
###############################################################################################################################


def simuler_colonie(graphe: matrice[float],                     
                    pheromones: matrice[float],                     
                    visibilite: matrice[float],                     
                    nb_fourmis: int,                     
                    alpha: float, beta: float)-> tuple[list[chemin], list[float]]:
    """    
    Simule le parcours de nb_fourmis fourmis d'une colonie lancées l'une après l'autre     
    dans le graphe. Renvoie la liste des cyles obtenus, ainsi que la liste des distances     
    correspondantes        
    >>> random.seed(54)     
    >>> g = get_graphe_exemple()    
    >>> n = len(g)    
    >>> simuler_colonie(g, init_pheromones(n), calculer_visibilite(g), 5, 1, 2)    
    ([[1, 0, 2, 3, 1], [3, 1, 0, 2, 3], [3, 2, 1, 0, 3], [1, 0, 3, 2, 1], [0, 1, 3, 2, 0]], [23, 23, 26, 26, 23])    
    """
    chemins = []
    distances = []

    for _ in range(nb_fourmis):
        chemin, distance = parcours_fourmi(graphe, pheromones, visibilite, alpha, beta)
        chemins.append(chemin)
        distances.append(distance)

    return (chemins, distances)


if __name__ == "__main__":
    doctest.testmod()