import graphviz
from . import graphe_no
from . import graphe_oriente


def genere_image(g, poids: bool = False) -> None:
    if isinstance(g, dict):
        dot = graphviz.Digraph(format='png')
        sommets = graphe_oriente.sommets(g)
        matrice = graphe_oriente.get_matrice_adjacence(g)
    elif isinstance(g, tuple):
        dot = graphviz.Graph(format='png')
        sommets = graphe_no.sommets(g)
        matrice = graphe_no.matrice(g)


    # Obtenir les sommets et la matrice d'adjacence

    # Ajouter les nœuds
    for sommet in sommets:
        dot.node(sommet)

    # Ajouter les arêtes en utilisant la matrice d'adjacence
    for i, ligne in enumerate(matrice):
        for j, w in enumerate(ligne):
            if w != 0:
                if isinstance(g, dict) or (isinstance(g, tuple) and i>=j):
                    dot.edge(sommets[i], sommets[j], label=str(w) if poids else "")


    # Générer le fichier PNG
    dot.render('graphe', cleanup=True)


if __name__ == "__main__":
    g= graphe_no.creer()
    graphe_no.set_arete("A", "B", g)
    graphe_no.set_arete("B", "C", g)
    graphe_no.set_arete("C", "A", g)
    genere_image(g)    