# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:25:19 2020

@author: Propriétaire
"""

import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
#           Initialisation des données
#------------------------------------------------------------------------------

reactif_titre=input("Entrer le nom du réactif titré :" ) 
Nb_stoech1 = int(input("Entrer le nombre stoechiométrique du réactif titré :"))   #  nombre stoechiométrique du réactif 1
reactif_titrant=input("Entrer le nom du réactif titrant :" ) 
Nb_stoech2 = int(input("Entrer le nombre stoechiométrique du réactif titrant :"))     #  nombre stoechimétrique du réactif 2
V1 = float(input("Entrer le volume V1 en mL de solution à titrer : ")) #  Volume initial de solution titrée en mL
C2= float(input("Entrer la concentration en mol/Lde réactif titrant :"))       #  concentration de la soltuion titrante en mol/L
V2_max=25       #  Volume maximal de solution titrante versé en mL
Vbe = float(input("Entrer le volume de solution titrante versé à l'équivalence :"))

#------------------------------------------------------------------------------
#  Calcul de la concentration de réactif titré
#------------------------------------------------------------------------------

C1= Nb_stoech1*C2*Vbe/(Nb_stoech2*V1)

print("La concentration de réactyif titré est : ", C1 ," mol/L.")
print()

#------------------------------------------------------------------------------
#  Création de listes pour faciliter les tracés de courbes
#------------------------------------------------------------------------------


V2_verse=[] # liste contenant l'abscisse c'est-à-dire le volume de solution titrante
N1=[]   # liste contenant les quantités de matière de réactif titré
N2=[]   # liste contenant les quantités de matière de réactif titrant

#------------------------------------------------------------------------------
#   Boucle simulant l'ajout d'un volume V2 de solution titrante:
# Pour chaque ajout de solution titrante, le programme calcule les quantités 
#   de matière des réactifs titrant et titré.
#------------------------------------------------------------------------------

for V2 in range(V2_max+1):
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


#Tracé du nuage de points
plt.plot(V2_verse,N1,"rx",label=reactif_titre) 
plt.plot(V2_verse,N2,"bx",label=reactif_titrant) 


#Titres des axes et du graphique
plt.title("Evolution des quantités des réactifs\n en fonction du volume V2 versé",color='black')
plt.ylabel('Quantité de matière')#nom de l'axe des ordonnées
plt.xlabel("volume V2 de solution titrante versé")#nom des axes des abscisses

#affichage de la légende
plt.legend()








