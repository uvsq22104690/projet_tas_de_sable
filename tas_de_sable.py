#########################################
# groupe MI 4
# Vincent BEAUVALLET
# Marjorie ADAM
# Levi HOIMIAN
# Kévin JOSEPH
# https://github.com/uvsq-info/l1-python
#########################################

####################import modules
import tkinter as t 
import random as r
import copy as c
####################variables globales 
X = 50
Y = 50
D = 25
clr = 0
taille = 10
configuration_courante = []
liste1 = ''
liste2 = ''
sauvegarde = []
sauvegarde1 = c.deepcopy(sauvegarde)
sauvegarde2 = c.deepcopy(sauvegarde)
####################constantes
HEIGHT = 500
WIDTH = 400
####################fonctions
def grille_vide():
    '''créer une configuration vide et l'affiche'''
    global configuration_courante, taille, clr
    global X, Y, D 
    configuration_courante = [[0] * taille for l in range(taille)]
    affiche_grille()
    return configuration_courante

def config_aleatoire():
    '''créer une configuration aléatoire et l'affiche'''
    global configuration_courante, taille, clr
    global X, Y, D
    if configuration_courante == []:
        configuration_courante = [[0] * taille for l in range(taille)]
    for i in range(taille):
        for j in range(taille):
            configuration_courante[i][j] = r.randint(0, 3)
    affiche_grille()
    return configuration_courante

def affiche_grille():
    '''sert à afficher une configuration'''
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
    return configuration_courante

def addition_config(liste1, liste2):
    '''additionne deux configurations'''
    taillemax = max(len(liste1), len(liste2))
    for i in range(taillemax):
        for j in range(taillemax):
            configuration_courante[i][j] = liste1[i][j] + liste2[i][j]
    affiche_grille()
    return configuration_courante

def soustraction_config(liste1, liste2):
    '''soustrait deux configurations'''
    taillemax = max(len(liste1), len(liste2))
    for i in range(taillemax):
        for j in range(taillemax):
            if liste1[i][j] - liste2[i][j] < 0:
                configuration_courante[i][j] = 0
            else:
                configuration_courante[i][j] = liste1[i][j] - liste2[i][j]
    affiche_grille()
    return configuration_courante

def save_config():
    '''sauvegarde une configuration sur l'une de vos trois sauvegardes'''
    global sauvegarde, sauvegarde1, sauvegarde2, configuration_courante
    if sauvegarde == []:
        sauvegarde = c.deepcopy(configuration_courante)
    elif sauvegarde != [] and sauvegarde1 == []:
        sauvegarde1 = c.deepcopy(configuration_courante)
    elif sauvegarde != [] and sauvegarde1 != [] and sauvegarde2 == []:
        sauvegarde2 = c.deepcopy(configuration_courante)
    else:
        pass
    return sauvegarde, sauvegarde1, sauvegarde2
        
def pile_centree(N):
    '''une grille vide avec un nombre N de grains de sables au milieu'''
    global taille
    configuration_pilecentree = [[0] * taille for l in range(taille)]
    configuration_pilecentree[taille // 2][taille // 2] = N
    stabilisation()
    affiche_grille()
    return configuration_pilecentree
            
def max_stable():
    '''une grille rempli de 3'''
    global taille
    configuration_maxstable = [[0] * taille for l in range(taille)]
    for i in range(taille):
        for j in range(taille):
            configuration_maxstable[i][j] = 3
    return configuration_maxstable

def config_random():
    '''une grille generé aléatoirement'''
    global taille
    configuration_random = [[0] * taille for l in range(taille)]
    for i in range(taille):
        for j in range(taille):
            configuration_random[i][j] = r.randint(0, 3)
    return configuration_random

def identity():
    global configuration_maxstable
    taille = 100
    configuration_identity = addition_config(configuration_maxstable, configuration_maxstable)
    stabilisation()
    return configuration_identity

def stabilisation():
    while True:
        trouve = False
        for r in range(taille):
                for c in range(taille):
                    if configuration_courante[r][c] > 3:
                        distribution(configuration_courante[r][c], r, c)
                        trouve = True
        if not trouve:
            return
        
def distribution(nbr, row, column):
    quotient, reste = divmod(nbr, 4)
    configuration_courante[row][col] = reste
    for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        configuration_courante[r][c] += quotient
    return


    



#########################GUI
racine = t.Tk()
racine.title('Projet Tas de Sable')
canvas = t.Canvas(racine, width=WIDTH, height=HEIGHT, bg='black')
boutonaleatoire = t.Button(racine, text='Créer config. aleatoire', command=config_aleatoire)
boutonvide = t.Button(racine, text='Affiche une grille vide', command=grille_vide)
boutonaddition = t.Button(racine, text='Additionner deux listes', command=lambda: addition_config(liste1, liste2))
boutonsoustraction = t.Button(racine, text='Soustraire deux listes', command=lambda: soustraction_config(liste1, liste2))
boutonsaveconfig = t.Button(racine, text='Sauvegarger config. actuelle', command=save_config)
boutonpilecentree = t.Button(racine, text='Pile centrée', command=pile_centree)
boutonmaxstable = t.Button(racine, text='Max Stable', command=max_stable)
boutonrandom = t.Button(racine, text='Random', command=config_random)
boutonidentity = t.Button(racine, text='Identity', command=identity)
choix1 = t.Listbox(racine)
choix1.insert(1, "Config Courante")
choix1.insert(2, "Config Pile Centrée")
choix1.insert(3, "Config Max Stable")
choix1.insert(4, "Config Random")
choix2 = t.Listbox(racine)
choix2.insert(1, "Config Courante")
choix2.insert(2, "Config Pile Centrée")
choix2.insert(3, "Config Max Stable")
choix2.insert(4, "Config Random")
#########################placement widget
canvas.grid(row=0, column=1, columnspan=2, rowspan=6)
boutonaleatoire.grid(row=0, column=0)
boutonvide.grid(row=1, column=0)
boutonaddition.grid(row=2, column=0)
boutonsoustraction.grid(row=3, column=0)
boutonsaveconfig.grid(row=4, column=0)
boutonpilecentree.grid(row=7, column=1)
boutonmaxstable.grid(row=7, column=2)
boutonrandom.grid(row=8, column=1)
boutonidentity.grid(row=8, column=2)
choix1.grid(row=0, column=4)
choix2.grid(row=1, column=4)
#########################mainloop
racine.mainloop()


