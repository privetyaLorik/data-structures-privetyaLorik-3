"""
Graphe non orienté
"""
type num = int | float

type matrice_adjacence = list[list[num]]

type liste_adjacence = dict[str, dict[str, num]]

# Dans ce fichier on modélise un graphe par une
# liste d'étiquettes de sommets et d'une matrice d'adjacence
type graphe = tuple[list[str], matrice_adjacence]


def creer() -> graphe:
    """Retourne un graphe vide (aucun sommet, aucune arête)"""
    return ([], [])


def sommets(g: graphe) -> list[str]:
    """Retourne la liste des sommets du graphe g."""
    return g[0]


def matrice(g: graphe):
    """Retourne la matrice d'adjacence du graphe g"""
    return g[1]


def index_sommet(s: str, g: graphe) -> int:
    """Renvoie l'indice du sommet s dans la liste des sommets du graphe g

    Lance une erreur si le sommet n'existe pas dans le graphe
    """
    return sommets(g).index(s)


def get_liste_adjacence(g: graphe) -> liste_adjacence:
    """Retourne la liste d'adjacence du graphe g."""
    etiquettes, matrice = g
    adjacence = {}

    for i, sommet in enumerate(etiquettes):
        adjacence[sommet] = {}
        for j, voisin in enumerate(etiquettes):
            if matrice[i][j] != 0:
                adjacence[sommet][voisin] = matrice[i][j]

    return adjacence


def nb_sommets(g: graphe):
    """renvoie le nombre de sommets de g"""
    return len(g[0])


def ajouter_sommet(s: str, g: graphe):
    """Ajoute une ligne et une colonne à la matrice du graphe
    Ajoute le sommet à sa liste de sommets"""

    g[0].append(s)

    for ligne in g[1]:
        ligne.append(0)

    nouvelle_ligne = [0] * len(g[0])
    g[1].append(nouvelle_ligne)


def set_arete(s1: str, s2: str, g: graphe, poids: num = 1):
    """Ajoute ou remplace l'arête s1-s2 dans le graphe g.
    Le poids vaut 1 par défaut"""
    if s1 not in sommets(g) or s2 not in sommets(g):
        raise ValueError("Un des sommets n'existe pas dans le graphe")

    i1 = index_sommet(s1, g)
    i2 = index_sommet(s2, g)

    g[1][i1][i2] = poids
    g[1][i2][i1] = poids


def get_voisins(s: str, g: graphe) -> list[tuple[str, num]]:
    """renvoie la liste des voisins du sommet s
    accompagnée du poids de l'arête associée"""
    if s not in sommets(g):
        raise ValueError("Le sommet n'existe pas dans le graphe")

    i = index_sommet(s, g)
    voisins = []

    for j, sommet in enumerate(sommets(g)):
        if g[1][i][j] != 0:
            voisins.append((sommet, g[1][i][j]))

    return voisins