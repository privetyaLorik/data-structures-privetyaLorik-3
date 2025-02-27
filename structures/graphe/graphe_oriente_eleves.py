type num = int|float

type matrice_adjacence = list[list[num]]

# Ici, on assimile directement le graphe à ses listes d'adjacence
type graphe = dict[str, dict[str, num]]

def creer() -> graphe:
    """Retourne un graphe vide (aucun sommet, aucune arête)"""
    return {}

def sommets(g: graphe) -> list[str]:
    """Retourne la liste des sommets du graphe g.
    """
    return list(g.keys())


def poids(s1: str, s2: str, g: graphe) -> num:
    """Retourne le poids de l'arête (s1, s2) si elle existe, sinon retourne None."""
    return g.get(s1, {}).get(s2, None)


def get_matrice_adjacence(g: graphe) -> matrice_adjacence:
    """
    Retourne la matrice d'adjacence du graphe g.

    >>> g = {"A": {"B": 1}, "B": {"A": 2, "C": 1}, "C": {"B": 3}}
    >>> get_matrice_adjacence(g)
    [[0, 1, 0], [2, 0, 1], [0, 3, 0]]
    """
    sommets_liste = list(g.keys())  
    taille = len(sommets_liste)
    
    matrice = [[0] * taille for _ in range(taille)]
    
    for i, s1 in enumerate(sommets_liste):
        for j, s2 in enumerate(sommets_liste):
            if s2 in g.get(s1, {}):
                matrice[i][j] = g[s1][s2]
    
    return matrice

        

def nb_sommets(g: graphe) -> int:
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
    g[s] = {}
    

def set_arc(s1:str, s2: str, g: graphe, poids: int|float = 1):
    """
    Ajoute un arc pondéré entre les sommets s1 et s2 du graphe g.
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
    g[s1].append(s2)


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
    pass


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
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    """
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
    """