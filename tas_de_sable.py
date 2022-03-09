#########################################
# groupe MI 4
# Vincent BEAUVALLET
# Marjorie ADAM
# Levi
# Kévin
# https://github.com/uvsq-info/l1-python
#########################################

####################import modules
import tkinter as t 
import random as r
####################variables globales 
X = 50
Y = 50
D = 25
clr = 0
taille = 10
configuration_courante = []
####################constantes
HEIGHT = 500
WIDTH = 400
####################fonctions
def grille_vide():
    global configuration_courante, taille, clr
    global X, Y, D 
    configuration_courante = [[0] * taille for l in range(taille)]
    affiche_grille()

def config_aleatoire():
    global configuration_courante, taille, clr
    global X, Y, D
    if configuration_courante == []:
        configuration_courante = [[0] * taille for l in range(taille)]
    for i in range(taille):
        for j in range(taille):
            configuration_courante[i][j] = r.randint(0, 3)
    affiche_grille()

def affiche_grille():
    global configuration_courante, taille, clr
    global X, Y, D
    for i in range(taille):
        for j in range(taille):
            if configuration_courante[i][j] == 0:
                clr = 'white'
            elif configuration_courante[i][j] == 1:
                clr = 'yellow'
            elif configuration_courante[i][j] == 2:
                clr = 'light green'
            elif configuration_courante[i][j] == 3:
                clr = 'light blue'
            else:
                clr = 'pink'
            canvas.create_rectangle(X, Y, X + D, Y + D, fill=clr, outline='black')
            X += 25
        X = 50
        Y += 25
#########################GUI
racine = t.Tk()
racine.title('Projet Tas de Sable')
canvas = t.Canvas(racine, width=WIDTH, height=HEIGHT, bg='purple')
boutonaleatoire = t.Button(racine, text='Créer config. aleatoire', command=config_aleatoire)
boutonvide = t.Button(racine, text='Affiche une grille vide', command=grille_vide)
#########################placement
canvas.grid(row=0, column=1, rowspan= 2)
boutonaleatoire.grid(row=0, column=0)
boutonvide.grid(row=1, column=0)
#########################mainloop
racine.mainloop()


