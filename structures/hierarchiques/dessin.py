from graphviz import Digraph
import arbrebin_mutable as ab

def show(arbre: ab.ArbreBin, viewer: bool = False):
    def ajoute(arbre: ab.ArbreBin, graphe: Digraph):
        if arbre is not None:
            node_id = str(id(arbre))
            value = str(arbre.data)  # Récupère la valeur du nœud

            graphe.node(node_id, label=value) 

            # Ajouter les liens pour le sous-arbre gauche et droit
            for enfant, label in zip((arbre.gauche, arbre.droite), ("G", "D")):
                if enfant is not None:
                    enfant_id = str(id(enfant))
                    graphe.edge(node_id, enfant_id, label=label)
                    ajoute(enfant, graphe)

    # Créer un graphe orienté
    graphe = Digraph(format='png')
    graphe.attr('node', shape='circle')

    # Ajouter les nœuds et les arêtes
    ajoute(arbre, graphe)

    # Afficher le graphe (par défaut, sauvegarde dans un fichier temporaire et affiche)
    if viewer:
        graphe.view(cleanup=True)
    else:
        graphe.render(cleanup=True)
