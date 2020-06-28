# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:25:19 2020

@author: Propriétaire
"""

import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
#           Initialisation des données
#   A modifier selon le dosage à réaliser
# Pour interroger l'utilisatuer et changer de dosage voir p 67 Belin
#------------------------------------------------------------------------------
Nb_stoech1=1     #  nombre stoechimétrique du réactif 1
Nb_stoech2=2     #  nombre stoechimétrique du réactif 2
V1 = 5          #  Volume initial de solution titrée en mL
C1 = 0.01       #  concentration de la soltuion titrée en mol/L
C2= 0.01        #  concentration de la soltuion titrante en mol/L
V2_max=25       #  Volume maximal de solution titrante versé en mL
reactif_titré="I2"
reactif_titrant="ion disulfate"
Vbe= Nb_stoech2*C1*V1/(Nb_stoech1*C2) # Volume versé à l'équivalence
print("Le volume à l'équivalence est : ", Vbe ," mL.")
print()

#------------------------------------------------------------------------------
#  Création de listes pour faciliter les tracés de courbes
#------------------------------------------------------------------------------


V2_verse=[] # liste contenant l'abscisse c'est-à-dire le volume de solution titrante
N1=[]   # liste contenant les quantités de matière de réactif titré
N2=[]   # liste contenant les quantités de matière de réactif titrant

#------------------------------------------------------------------------------
#   Boucle simulant l'ajout d'un volume V2 de solutoion titrante:
# Pour chaque ajout de solution titrante, le programme calcule les quantités 
#   de matière des réactifs titrant et titré.
#------------------------------------------------------------------------------

for V2 in range(V2_max):
    N1_init=C1*V1/1000   #Quantité de matière initiale de réactif titré
    N2_verse=C2*V2/1000   #Quantité de matière de réactif titrant versé
    V2_verse.append(V2)  # On ajoute V2 dans la liste
    
    if V2<Vbe:  # Avant l'équivalence
        N2.append(0)
        N1_restant=N1_init-Nb_stoech1*N2_verse/Nb_stoech2
        N1.append(N1_restant)
    else:  # après l'équivalence
        N1.append(0)
        N2_restant=C2*V2/1000-Nb_stoech2*N1_init/Nb_stoech1
        N2.append(N2_restant)

#--------------------------------------------------------------------------
#  Affichage des listes contenant les quantités de matière
#--------------------------------------------------------------------------
print("Quantités de réactif titré au cours du titrage (en mol) : ")
print(N1)
print()
print("Quantités de réactif titrant au cours du titrage (en mol) : ")
print(N2)
#------------------------------------------------------------------------------
#           Tracé du graphique
#------------------------------------------------------------------------------
# ici on veut dire d'utiliser
# pour l'axe des X : entre 0 et 25
# pour l'axe des Y : entre 0 et max (des quantités initiales)
plt.axis([0, 25, 0, max(N1_init,N2_verse)])

#Tracé du nuage de points
plt.plot(V2_verse,N1,"rx",label="I2") 
plt.plot(V2_verse,N2,"bx",label="ion_thiosulfate") 


#Titres des axes et du graphique
plt.title("Dosage du diiode par les ions thiosulfate",color='r')
plt.ylabel('Quantité de matière')#nom de l'axe des ordonnées
plt.xlabel("volume d'ion thiosulfate versé")#nom des axes des abscisses

#affichage de la légende
plt.legend()









