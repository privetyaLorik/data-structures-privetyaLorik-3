from structures.graphe import graphe_no
from structures.lineaires import files
from structures.lineaires import pile

def bfs(s:str,g:graphe_no.graphe):
    f= files.creer()
    dej= [s]
    files.enfiler(s)
    while not files.est_vide(f):
        a = files.defiler(f)
        print(a)
        for e in graphe_no.get_voisins(a,g):
            if e not in dej:
                files.enfiler(e,g)
                dej.append(e)

def dfs(g: graphe_no.graphe, depart: str):
    p = pile.creer()
    dej = [depart]
    pile.empiler(p, depart)
    while not pile.est_vide(p):
        a = pile.depiler(p)
        print(a)
        for e in graphe_no.get_voisins(a, g):
            if e not in dej:
                pile.empiler(p, e)
                dej.append(e)

def est_connexe(g: graphe_no.graphe) -> bool:
    s = g[0]
    liste = bfs(s)
    return liste == graphe_no.sommets(g)

def sous_graphe(sommets: list[str], g: graphe_no.graphe) -> graphe_no.graphe:
    new_g = graphe_no.creer()
    for s in sommets:
        graphe_no.ajouter_sommet(new_g, s)
    for s in sommets:
        for voisin in graphe_no.get_voisins(g, s):
            if voisin in sommets:  
                graphe_no.set_arete(new_g, s, voisin)

    return new_g