#########################################
# groupe MI 4
# Vincent BEAUVALLET
# Marjorie ADAM
# Levi
# Kévin
# https://github.com/uvsq-info/l1-python
#########################################

###############################librairies
import tkinter as tk
###############################variables globales
config_courante = [[], [], [], [], []]
###############################fonctions
def configuration_courante():
    """Initialise et retourne la configuration courante"""
    config_courante = [["", "#", "#", "#", ""], ["#", 1, 1, 1, "#"], ["#", 1, 1, 1, "#"], ["#", 1, 1, 1, "#"], ["", "#", "#", "#", ""]]
    return config_courante

def configuration_vide():
    """Retourne une configuration vide"""
    config_courante = [["", "#", "#", "#", ""], ["#", "", "", "", "#"], ["#", "", "", "", "#"], ["#", "", "", "", "#"], ["", "#", "#", "#", ""]]
    return configuration_vide
###############################programme principale
racine = tk.Tk()
canvas = tk.Canvas(racine, width=500, height=500)
bouton = tk.Button(racine, text="Config.Aleatoire")
canvas.pack()
bouton.pack()
racine.mainloop()


