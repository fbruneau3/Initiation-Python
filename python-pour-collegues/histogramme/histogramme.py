# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:40:19 2020

@author: Utilisateur
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

nb_mesures=int(input("Combien y a-t-il de groupes? "))



#Création d'un dictionnaire contenant les valeurs de pH
pH = []
with open('mesures_ph.csv', newline='') as csvfile:
    file = csv.DictReader(csvfile, delimiter=";")
    for ligne in file:
        pH.append(dict(ligne))

print(np.array(pH))


liste_pH1=[]
liste_pH2=[]
liste_pH3=[]
for groupe in pH:
    liste_pH1.append(float(groupe['pH1']))
    liste_pH2.append(float(groupe['pH2']))
    liste_pH3.append(float(groupe['pH3']))
    
plt.figure(1)
plt.hist(liste_pH1,color='b')
plt.ylabel('Fréquence')
plt.xlabel('pH1')
plt.title("Mesures de pH1 effectuées par "+str(nb_mesures)+" groupes.")
plt.figure(2)
plt.hist(liste_pH2,color='r')
plt.ylabel('Fréquence')
plt.xlabel('pH2')
plt.title("Mesures de pH2 effectuées par "+str(nb_mesures)+" groupes.")
plt.figure(3)
plt.hist(liste_pH3,color='g')
plt.ylabel('Fréquence')
plt.xlabel('pH3')
plt.title("Mesures de pH3 effectuées par "+str(nb_mesures)+" groupes.")
