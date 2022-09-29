#!/usr/bin/env python3

#Lire la saisie de l'utilisateur
min = int(input("Entrez le min : 1))
max = int(input("Entrez le max : 100000))
for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
