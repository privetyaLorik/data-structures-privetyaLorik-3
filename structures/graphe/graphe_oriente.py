type num = int|float

type matrice_adjacence = list[list[int|float]]

# Ici, on assimile directement le graphe à ses listes d'adjacence
type graphe = dict[str, dict[str, int|float]]

def creer() -> graphe:
    """Retourne un graphe vide (aucun sommet, aucune arête)"""
    return {}

def sommets(g: graphe) -> list[str]:
    """Retourne la liste des sommets du graphe g.
    """
    return list(g.keys())

def poids(s1: str, s2: str, g: graphe) -> num:
    return g[s1][s2]


def get_matrice_adjacence(g: graphe) -> matrice_adjacence:
    """
    Retourne la matrice d'adjacence du graphe g.

    >>> g = {"A": {"B": 1}, "B": {"A": 2, "C": 1}, "C": {"B": 3}}
    >>> get_matrice_adjacence(g)
    [[0, 1, 0], [2, 0, 1], [0, 3, 0]]
    """
    return [[g[s1].get(s2, 0) for s2 in sommets(g)] for s1 in sommets(g)]


def nb_sommets(g: graphe):
    """Nombre de sommets du graphe g
    """
    return len(g)

def ajouter_sommet(s: str, g: graphe):
    """
    Ajoute un sommet s au graphe g si il n'existe pas déjà.

    >>> g = creer()
    >>> ajouter_sommet("A", g)
    >>> sommets(g)
    ['A']
    >>> ajouter_sommet("A", g)
    >>> sommets(g)
    ['A']
    >>> ajouter_sommet("B", g)
    >>> sommets(g)
    ['A', 'B']
    """
    if s not in g:
        g[s]={}
    
def set_arc(s1:str, s2: str, g: graphe, poids: int|float = 1):
    """
    Ajoute une arête orientée pondérée entre les sommets s1 et s2 du graphe g.
    Si les sommets n'existent pas, ils sont ajoutés au graphe.
    Met à jour la matrice d'adjacence pour refléter les changements.

    >>> g = creer()
    >>> set_arc('A', 'B', g, 3)
    >>> get_matrice_adjacence(g)
    [[0, 3], [0, 0]]
    >>> set_arc('B', 'A', g, 2)
    >>> get_matrice_adjacence(g)
    [[0, 3], [2, 0]]
    >>> set_arc('C', 'D', g, 5)
    >>> get_matrice_adjacence(g)
    [[0, 3, 0, 0], [2, 0, 0, 0], [0, 0, 0, 5], [0, 0, 0, 0]]
    >>> set_arc('A', 'C', g, 4)
    >>> get_matrice_adjacence(g)
    [[0, 3, 4, 0], [2, 0, 0, 0], [0, 0, 0, 5], [0, 0, 0, 0]]
    """

    ajouter_sommet(s1, g)
    ajouter_sommet(s2, g)
    g[s1][s2]=poids


def get_successeurs(s: str, g: graphe) -> list[str]:
    """
    Retourne la liste des sommets sortants du sommet s dans le graphe g.

    >>> g = {"A": {"B": 1}, "B": {"A": 2, "C": 1}, "C": {"B": 3}}
    >>> get_successeurs("A", g)
    ['B']
    >>> get_successeurs("B", g)
    ['A', 'C']
    >>> get_successeurs("C", g)
    ['B']
    """
    return list(g[s].keys())


def get_predecesseurs(s: str, g: graphe) -> list[str]:
    """
    Retourne la liste des sommets entrants du sommet s dans le graphe g.

    >>> g = {"A": {"B": 1}, "B": {"A": 2, "C": 1}, "C": {"B": 3}}
    >>> get_predecesseurs("A", g)
    ['B']
    >>> get_predecesseurs("B", g)
    ['A', 'C']
    >>> get_predecesseurs("C", g)
    ['B']
    >>> get_predecesseurs("D", g)
    []
    """
    return [entrant for entrant in g if s in g[entrant]]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    from . import dessin

    g = creer()
    set_arc("A", "B", g, 5)
    set_arc("B", "C", g, 8)
    set_arc("C", "D", g, 9)
    set_arc("D", "E", g, 2)
    set_arc("F", "A", g, 1)
    set_arc("A", "C", g, 2)
    set_arc("B", "D", g ,7)
    set_arc("E", "C", g, 9)
    set_arc("E", "E", g, 9)
    dessin.genere_image(g, True)