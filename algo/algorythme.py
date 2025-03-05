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
    return liste == graphe_no.get_(g)


