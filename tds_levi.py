import tkinter as tk
from random import randint
from turtle import update

dimension = 10
mesure = 500
dim_case = mesure // dimension

#Creation de la palette de couleurs
color1 = "#FF4000"
color2 = "#FF6000"
color3 = "#FF8000"
color4 = "#FFA000"
color5 = "#FFC000"
color6 = "#FFE000"
color7 = "#FFEF00"
color8 = "#FFFFFF"

#initialisation de la configuration courante
configuration_courante = []
for a in range(dimension+2):
    if a == 0 or a == dimension+1:
        configuration_courante.append(['#']*(dimension+2))
    else:
        configuration_courante.append(['#']+[0]*dimension+['#'])

#Fonction qui permet de remttre chaque case du tas de sable à 0
def clear(matrice):
    for i in range(1, dimension+1):
        for j in range(1, dimension+1):
            matrice[i][j] = 0

#Fonction qui permet de remplir chaque case avec entre 0 et 7 grains de sable
def shuffle(matrice):
    for i in range(1, dimension+1):
        for j in range(1, dimension+1):
            matrice[i][j] = randint(0,7)

#Fonction qui remplis le canvas de cases leur attribuant chacune une couleur en fonction de la quantité de grains presents
def affichage(matrice):
    for i in range(1, dimension+1):
        for j in range(1, dimension+1):
            if matrice[j][i] == 0:
                color = color8
            if matrice[j][i] == 1:
                color = color7
            if matrice[j][i] == 2:
                color = color6
            if matrice[j][i] == 3:
                color = color5
            if matrice[j][i] == 4:
                color = color4
            if matrice[j][i] == 5:
                color = color3
            if matrice[j][i] == 6:
                color = color2
            if matrice[j][i] == 7:
                color = color1
            canvas.create_rectangle((i*dim_case-dim_case, j*dim_case-dim_case),((i+1)*dim_case, (j+1)*dim_case), fill=color)

#Fonction qui met à jour la configuration courante apres une etape d'ecoulement du tas de sable 
def ecoulement(matrice):
    listx=[]
    listy=[]
    for y in range(1,dimension+1):
        for x in range(1,dimension+1):
            if matrice[y][x] >= 4:
                listy.append(y)
                listx.append(x)
                matrice[y][x] -= 4
    for i in range(len(listx)):
        x = listx[i]
        y = listy[i]
        if matrice[y+1][x] != '#':
            matrice[y+1][x] += 1

        if matrice[y-1][x] != '#':
            matrice[y-1][x] += 1

        if matrice[y][x+1] != '#':
            matrice[y][x+1] += 1

        if matrice[y][x-1] != '#':
            matrice[y][x-1] += 1
    return matrice

#Création de la fenêtre racine
racine = tk.Tk()

#creation des canvas et boutons 
canvas = tk.Canvas(racine, height=mesure, width=mesure)
bouton1 = tk.Button(racine, text="shuffle", command=lambda : shuffle(configuration_courante))
bouton2 = tk.Button(racine, text="initialisation", command=lambda : clear(configuration_courante))
bouton3 = tk.Button(racine, text="ecoulement", command=lambda : ecoulement(configuration_courante))

#positionnement des canvas et boutons 
canvas.grid(row=0, column=1)
bouton1.grid(row=0, column=0)
bouton2.grid(row=2, column=0)
bouton3.grid(row=3, column=0)

#La boucle principale est ici car je ne sais pas comment animer autrement
while True:
    canvas.update()
    affichage(configuration_courante)

    
racine.mainloop() # Lancement de la boucle principale

#Deuxieme version:

"""
import tkinter as tk
from random import randint
from turtle import update

color1 = "#FF2000"
color2 = "#FF4000"
color3 = "#FF6000"
color4 = "#FF8000"
color5 = "#FFA000"
color6 = "#FFC000"
color7 = "#FFE000"
color8 = "#FFFF00"

dimension = 10

tas = []
mesure = 500
dim_case = mesure // dimension

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, height=mesure, width=mesure)
canvas.grid()

for a in range(dimension+2):
    if a == 0 or a == dimension+1:
        tas.append(['#']*(dimension+2))
    else:
        tas.append(['#']+[0]*dimension+['#'])

for i in range(1, dimension+1):
    for j in range(1, dimension+1):
        tas[i][j] = randint(0,7)


def affichage(matrice):
    for i in range(1, dimension+1):
        for j in range(1, dimension+1):
            if matrice[j][i] == 0:
                color = color8
            if matrice[j][i] == 1:
                color = color7
            if matrice[j][i] == 2:
                color = color6
            if matrice[j][i] == 3:
                color = color5
            if matrice[j][i] == 4:
                color = color4
            if matrice[j][i] == 5:
                color = color3
            if matrice[j][i] == 6:
                color = color2
            if matrice[j][i] == 7:
                color = color1
            canvas.create_rectangle((i*dim_case-dim_case, j*dim_case-dim_case),((i+1)*dim_case, (j+1)*dim_case), fill=color)


def ecoulement(tab):
    listx=[]
    listy=[]
    a = 0
    for y in range(1,dimension+1):
        for x in range(1,dimension+1):
            if tab[y][x] >= 4:
                listy.append(y)
                listx.append(x)
                tab[y][x] -= 4
    for i in range(len(listx)):
        x = listx[i]
        y = listy[i]
        if tab[y+1][x] != '#':
            tab[y+1][x] += 1

        if tab[y-1][x] != '#':
            tab[y-1][x] += 1

        if tab[y][x+1] != '#':
            tab[y][x+1] += 1

        if tab[y][x-1] != '#':
            tab[y][x-1] += 1
    return tab

affichage(tas)
while True:
    canvas.update()
    affichage(ecoulement(tas))

racine.mainloop() # Lancement de la boucle principale
"""