import math
try:
    T= float (input ("entre la température de congélation"))
    N = float(input("entrer la number of molecules formes per molecule of solute  "))
    Y = 1.858
    m = float (input ("entrer la valeur de la molalité "))
    nu= float (input ("enter la valeur de nu"))
    M = 18.01528
except:
    print("pas exacte")
P = (N*Y*m)
PHi = (T/P)
Z = nu*M*m
a =-(PHi*Z/1000)
aw = math.exp(a)
print("valeur de aw =", aw)
