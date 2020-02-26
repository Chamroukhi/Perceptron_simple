"""
          #!/usr/bin/env python3
          # -*- coding: utf-8 -*-
          Created on Sun Feb 25 21:36:54 2020

             @author: CHAMROUKHI Naoufel

           Perceptron simple (un seul neurone)
             Apprentissage de la fonction
                  Non(Non logique )
"""
 
import numpy as np

#base d'apprentissage X ==> Feautures ; Y ==> Target
x =np.array( [[0], [1]])
y = np.array([[1], [0]])

#Initialisation les poids Wi à 0 ainsi que le biais à 1
biais=1
w0= 0
w1= 0

#taux_dapprentissage 
taux_dapprentissage=0.1

#nombre d'itérations
nb_itération=8

#nombre d'observations= 4 ; [0, 0], [0, 1], [1, 0], [1, 1] 
nb_observation=2


#Définir La fonction Heaviside{si sortie s<=0; Heaviside(s)=0, si non Heaviside(s)=1}
def Heaviside(a):
    if a>0: 
        r=1
    elif a<=0:
        r=0
    return r


for n in range(nb_itération):
    for xi in range(nb_observation): 
        
        #calculer la sortie s (sortie obtenue)
        s=((biais*w0)+(x[xi]*w1))
        S=Heaviside(s)
        
        #si la sortie obtenue(S) != la sortie réelle (y)) => mettre à jour les poids
        #Wi=Wi+taux_dapprentissage*(y-S)*Xi;
        if (y[xi]!=S):
           w0=float(w0+taux_dapprentissage*(int(y[xi])-S)*biais)
           w1=float(w1+taux_dapprentissage*(int(y[xi])-S)*x[xi])
           
                
                
            
#cette partie pour faire de la prédiction d'une observation P
X=0
          
P =(biais*w0)+(X*w1)
print("====================== Prédiction ====================\n")
print("                pour X =",X)
print("                     Y =",Heaviside(P))         
print("\n======================================================")

print("Les nouvelles valeurs de poids synaptiques Wi :")
print("W0 = ",w0,"\nW1 =",w1,)
print("\n======================================================")