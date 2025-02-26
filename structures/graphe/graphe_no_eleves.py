def recherche_binaire(liste, element):
    gauche = 0
    droite = len(liste) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu] == element:
            return milieu
        elif liste[milieu] < element:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1 


liste_textes = [
    "Bonjour",
    "Python est puissant",
    "Liste de chaînes",
    "Programmation",
    "Intelligence artificielle",
    "ChatGPT",
    "Exemple de texte",
    "Développement logiciel",
    "Codage et algorithmes",
    "Apprentissage automatique",
    "Données structurées",
    "Variables et fonctions",
    "Boucles et conditions",
    "Programmation orientée objet",
    "Interface utilisateur",
    "Conception et architecture",
    "Test et débogage",
    "Optimisation du code",
    "Compilation et interprétation",
    "Gestion de projet",
    "Systèmes embarqués",
    "Automatisation des tâches",
    "Sécurité informatique",
    "Cloud computing",
    "Langages de programmation"
]
print(recherche_binaire(liste_textes,"l" ))