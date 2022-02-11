#########################################
# groupe MI 4
# Vincent
# Marjorie
# Levi
# Kévin
# https://github.com/uvsq-info/l1-python
#########################################

configuration_courante= [[,"#","#","#",], ["#",a,b,c,"#"], ["#",d,e,f,"#"], ["#",g,h,i,"#"], [,"#","#","#",]]
grain_a: 0
grain_b: 0
grain_c: 0
grain_d: 0
grain_e: 0
grain_f: 0
grain_g: 0
grain_h: 0
grain_i: 0


import random as rd
import tkinter as tk

def configuration_aleatoire:
    """                            """
    pass

def affiche_grille:
    """                            """
    pass

def avalanche:
    """                            """
    pass


racine = tk.Tk()
canvas = tk.Canvas(racine, )
bouton = tk.Button(racine, text="Config.Aléatoire", command=configuration_aleatoire)
canvas.pack()
bouton.pack()
racine.mainloop()



