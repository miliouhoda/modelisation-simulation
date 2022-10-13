import math
try:
    Tf = float(input("Entrez la valeur de Tf en K: "))
    R = 8.314
    H = 6009.5
    C = 37.87
except:
    print("la valeur entree n'est pas un nombre")
A= -H/R
B=(1/Tf)
C=(1/273.15)
D=-C/R
M=Tf-273.15
N=M/Tf
K=Tf/(273.15)
j=math.log(K)
L=(A*(B-C))+(D*(N-j))
aw=math.exp(L)
print("valeur de l'activite de l'eau =", aw)




