#structures/graphes/graphe_no.py
#uv run -m structures.graphes.graphe_no

"""
Graphe non orienté
"""
type num = int|float

type matrice_adjacence = list[list[num]]

type liste_adjacence = dict[str, dict[str, num]]

# Dans ce fichier on modélise un graphe par une
# liste d'étiquettes de sommets et d'une matrice d'adjacence
type graphe = tuple[list[str], matrice_adjacence]


def creer() -> graphe:
    """Retourne un graphe vide (aucun sommet, aucune arête)"""
    return ([], [])


def sommets(g: graphe) -> list[str]:
    """Retourne la liste des sommets du graphe g.
    """
    return g[0]

def matrice(g: graphe):
    """Retourne la matrice d'adjacence du graphe g
    """
    return g[1]

def nb_sommets(g: graphe) -> int:
    """renvoie le nombre de sommets de g"""
    return len(sommets(g))


def poids(s1: str, s2: str, g: graphe) -> num:
    """
    Retourne le poids de l'arête entre les sommets s1 et s2 dans le graphe g.

    >>> g = (['A', 'B', 'C'], [[0, 2, 0], [2, 0, 3], [0, 3, 0]])
    >>> poids('A', 'B', g)
    2
    >>> poids('B', 'C', g)
    3
    >>> poids('A', 'C', g)
    0
    """
    return matrice(g)[index_sommet(s1, g)][index_sommet(s2, g)]


def index_sommet(s: str, g: graphe) -> int:
    """Renvoie l'indice du sommet s dans la liste des sommets du graphe g
    
    Lance une erreur si le sommet n'existe pas dans le graphe
    
    >>> g = (['A', 'B', 'C'], [[0, 2, 0], [2, 0, 3], [0, 3, 0]])
    >>> index_sommet('A', g)
    0
    >>> index_sommet('B', g)
    1
    >>> index_sommet('C', g)
    2
    >>> index_sommet('D', g)
    Traceback (most recent call last):
    ...
    ValueError: 'D' is not in list
    """
    return sommets(g).index(s)


def get_liste_adjacence(g: graphe) -> liste_adjacence:
    """Retourne la liste d'adjacence du graphe g. ALGO A CONNAITRE
    
    >>> g = (['A', 'B', 'C'], [[0, 2, 0], [2, 0, 3], [0, 3, 0]])
    >>> get_liste_adjacence(g)
    {'A': {'B': 2}, 'B': {'A': 2, 'C': 3}, 'C': {'B': 3}}
    """
    return {s1: {s2: matrice(g)[index_sommet(s1, g)][index_sommet(s2, g)] 
                 for s2 in sommets(g)
                 if matrice(g)[index_sommet(s1, g)][index_sommet(s2, g)]!=0
                 } 
            for s1 in sommets(g)}



def ajouter_sommet(s: str, g: graphe):
    """Ajoute une ligne et une colonne à la matrice du graphe
    Ajoute le sommet à sa liste de sommets
    
    >>> g = (['A', 'B'], [[0, 1], [1, 0]])
    >>> ajouter_sommet('C', g)
    >>> sommets(g)
    ['A', 'B', 'C']
    >>> matrice(g)
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    """
    sommets(g).append(s)
    for ligne in matrice(g):
        ligne.append(0)
    matrice(g).append([0 for _ in range(nb_sommets(g))])


def set_arete(s1:str, s2: str, g: graphe, poids: num = 1):
    """Ajoute ou remplace l'arête s1-s2 dans le graphe g.
    Le poids vaut 1 par défaut

    >>> g = (['A', 'B'], [[0, 0], [0, 0]])
    >>> set_arete('A', 'B', g, 3)
    >>> matrice(g)
    [[0, 3], [3, 0]]
    >>> set_arete('B', 'C', g, 2)
    >>> matrice(g)
    [[0, 3, 0], [3, 0, 2], [0, 2, 0]]
    """

    if s1 not in sommets(g):
        ajouter_sommet(s1, g)
    if s2 not in sommets(g):
        ajouter_sommet(s2, g)
    matrice(g)[index_sommet(s1, g)][index_sommet(s2, g)] = poids
    matrice(g)[index_sommet(s2, g)][index_sommet(s1, g)] = poids


def get_voisins(s: str, g: graphe) -> list[str]:
    """renvoie la liste des voisins du sommet s    

    >>> g = (['A', 'B', 'C'], [[0, 2, 0], [2, 0, 3], [0, 3, 0]])
    >>> get_voisins('A', g)
    ['B']
    >>> get_voisins('B', g)
    ['A', 'C']
    >>> get_voisins('C', g)
    ['B']
    """
    return [s2 for s2 in sommets(g)
            if matrice(g)[index_sommet(s, g)][index_sommet(s2, g)] != 0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    from . import dessin

    g = creer()
    set_arete("A", "B", g)
    set_arete("B", "C", g)
    set_arete("C", "D", g)
    set_arete("D", "E", g)
    set_arete("E", "F", g)
    set_arete("F", "A", g)
    set_arete("A", "C", g)
    set_arete("B", "D", g)
    set_arete("E", "C", g)
    dessin.genere_image(g)
