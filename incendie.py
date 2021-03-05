#########################################
# groupe DLBI 1
# Kubilay MEYDAN
# Julie CIESLA
# Alix FRAGNER
# Margaux DUBOIS GUENRO
# Elise REBER
# https://github.com/uvsq-info/l1-python
#########################################

import tkinter as tk

racine = tk.Tk()
racine.title("Simulation D'incendie")


#Constantes

LARGEUR = 400
HAUTEUR = 400
COULEUR_QUADR = "blue"
COTE = 40

# création des fonctions


def quadrillage():
    """Affiche un quadrillage constitué de carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        terrain.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        terrain.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += COTE


# Création des widgets

terrain = tk.Canvas(racine, width=400, height=400, bg="red")
bouton_stop = tk.Button(racine, text="ARRETER")
bouton_start = tk.Button(racine, text="DEMARRER")
bouton_etape = tk.Button(racine, text="ETAPE SUIVANTE")
bouton_aleatoire = tk.Button(racine, text="GENERER UN TERRAIN ALEATOIRE")
bouton_fichier = tk.Button(racine, text="CHARGER UN TERRAIN A PARTIR D'UN FICHIER")
bouton_sauvegarder = tk.Button(racine, text="SAUVEGARDER")
label_nbre_parcelles = tk.Label(racine, bg="yellow")
label_nbre_etapes = tk.Label(racine, bg="blue")

# Positionnements des widgets

terrain.grid(row=1, rowspan=3, column=1, columnspan=3)
bouton_start.grid(row=1, column=0)
bouton_etape.grid(row=2, column=0)
bouton_stop.grid(row=3, column=0)
bouton_aleatoire.grid(row=0, column=1)
bouton_fichier.grid(row=0, column=2)
bouton_sauvegarder.grid(row=0, column=3)
label_nbre_parcelles.grid(row=4, column=1, columnspan=3)
label_nbre_etapes.grid(row=5, column=1, columnspan=3)

terrain.bind(quadrillage())

racine.mainloop()
