
"""
          #!/usr/bin/env python3
          # -*- coding: utf-8 -*-
          Created on Sun Feb 25 21:36:54 2020

             @author: CHAMROUKHI Naoufel

           Perceptron simple (un seul neurone)
             Apprentissage de la fonction
                  AND (ET logique)
"""
 
import numpy as np

#base d'apprentissage X ==> Feautures ; Y ==> Target
x =np.array( [[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

#Initialisation les poids Wi à 0 ainsi que le biais à 1
biais=1
w0= 0
w1= 0
w2= 0

#alpha 
alpha=0.1

#nombre d'itérations
nb_itération=8

#nombre d'observations= 4 ; [0, 0], [0, 1], [1, 0], [1, 1] 
nb_observation=4


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
        s=((biais*w0)+(x[xi,0]*w1)+(x[xi,1]*w2))
        S=Heaviside(s)
        
        #si la sortie obtenue(S) != la sortie réelle (y)) => mettre à jour les poids
        #Wi=Wi+alpha*(y-S)*Xi;
        if (y[xi]!=S):
           w0=float(w0+alpha*(int(y[xi])-S)*biais)
           w1=float(w1+alpha*(int(y[xi])-S)*x[xi,0])
           w2=float(w2+alpha*(int(y[xi])-S)*x[xi,1])
                
                
            
#cette partie pour faire de la prédiction d'une observation P
X1=1
X2=1            
P =(biais*w0)+(X1*w1)+(X2*w2)
print("====================== Prédiction ====================\n")
print("                pour X1 =",X1,",X2 =",X2)
print("                       Y =",Heaviside(P))         
print("\n======================================================")

print("Les nouvelles valeurs de poids synaptiques Wi :")
print("W0 =",w0,"\nW1 = ",w1,"\nW2 = ",w2)
print("\n======================================================")