import sys
sys.path.append("chemin/vers/le/dossier")
import arbrebin_mutable as ab
import dessin as dess 

def MinList(liste):
    """Renvoie l'élément avec la plus petite valeur dans la liste."""
    minimum = liste[0]
    for x in liste:
        if int(x[0][-1]) < int(minimum[0][-1]):
            minimum = x
    return minimum

def MinList2(liste):
    """Renvoie le deuxième plus petit élément dans la liste."""
    minimum = MinList(liste)
    second_minimum = None
    for x in liste:
        if x != minimum and (second_minimum is None or int(x[0][-1]) < int(second_minimum[0][-1])):
            second_minimum = x
    return second_minimum

def nomdesnoeux(N1: tuple, N2: tuple):
    """Combine deux nœuds pour former un nouveau nœud."""
    lettres_N1 = ''.join([char for char in N1[0] if not char.isdigit()])
    lettres_N2 = ''.join([char for char in N2[0] if not char.isdigit()])
    freq_N1 = int(''.join([char for char in N1[0] if char.isdigit()]))
    freq_N2 = int(''.join([char for char in N2[0] if char.isdigit()]))
    somme_freq = freq_N1 + freq_N2

    return (lettres_N1 + lettres_N2 + str(somme_freq), N1, N2)

def get_dicofreq(texte: str) -> dict[str, int]:
    """Renvoie un dictionnaire de fréquence des lettres dans le texte."""
    dico_freq = {}
    for char in texte:
        dico_freq[char] = dico_freq.get(char, 0) + 1
    return dico_freq

def get_arbre_huffman(dicofreq: dict[str, int]) -> tuple:
    """Construit l'arbre de Huffman à partir du dictionnaire de fréquences."""
    liste_feuille = [(str(char) + str(freq), None, None) for char, freq in dicofreq.items()]


    while len(liste_feuille) > 1:
   
        min1 = MinList(liste_feuille)
        liste_feuille.remove(min1)  
        min2 = MinList(liste_feuille)  
        liste_feuille.remove(min2)  


        nouveau_noeud = nomdesnoeux(min1, min2)

  
        liste_feuille.append(nouveau_noeud)


    return liste_feuille[0]


def Creer_arbre(noeud: tuple) -> ab.ArbreBin:
    """
    Convertit un nœud sous forme de tuple (valeur, nœud gauche, nœud droit)
    en un arbre binaire utilisant la classe ArbreBin.
    """

    if noeud[1] is None and noeud[2] is None:
        return ab.ArbreBin(noeud[0], None, None)
 
    gauche = Creer_arbre(noeud[1])  
    droite = Creer_arbre(noeud[2])  
    return ab.ArbreBin(noeud[0], gauche, droite)


arbre_huffman = get_arbre_huffman(get_dicofreq("MISSISSIPI RIVER"))
arbre_binaire = Creer_arbre(arbre_huffman)


print(arbre_binaire.data)  
print(arbre_binaire.est_feuille())  
dess.show(arbre_binaire)
