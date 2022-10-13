K1 = 4.2
K2 = 1.75
K3 = 0.74
K4 = 0.34
ksi = 0.1
Z1 = 0.1
Z2 = 0.2
Z3 = 0.3
Z4 = 0.4
Tf = 200
Pf = 100
F = 100
eps = 0.001
def RR (Z1, Z2, Z3,Z4, K1, K2, K3, K4):
    result = ((Z1*(1-K1))/(1+ksi*(K1-1)))+((Z2*(1-K2))/(1+ksi*(K2-1)))+((Z3*(1-K3))/(1+ksi*(K3-1)))+((Z4*(1-K4))/(1+ksi*(K4-1)))
    return result
def RRD (Z1, Z2, Z3, Z4, K1, K2, K3, K4):
    result = ((Z1*pow(1-K1, 2))/(pow(1+ksi*(K1-1), 2)))+((Z2*pow(1-K2, 2))/(pow(1+ksi*(K2-1), 2)))+((Z3*pow(1-K3, 2))/(pow(1+ksi*(K3-1), 2)))+((Z4*pow(1-K4, 2))/(pow(1+ksi*(K4-1), 2)))
    return result
Objectiffunction = RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4)
while abs(Objectiffunction) >= eps:
    ksi = ksi-((RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4))/(RRD(Z1, Z2, Z3, Z4, K1, K2, K3, K4)))
    Objectiffunction = RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4)
print (" ksi ", " est =", ksi)
print("valeur de la fonction objectif est =", Objectiffunction)

V = F*ksi
print ("la valeur de V est =", V)
x1 = Z1/(1+ksi*(K1-1))
print ("la valeur de x1 est =", x1)
x2 = Z2/(1+ksi*(K2-1))
print ("la valeur de x2 est =", x2)
x3 = Z3/(1+ksi*(K3-1))
print ("la valeur de x3 est =", x3)
x4 = Z4/(1+ksi*(K4-1))
print ("la valeur de x4 est =", x4)
y1 = x1*K1
print ("la valeur de y1 est =", y1)
y2 = x2*K2
print ("la valeur de y2 est =", y2)
y3 = x3*K3
print ("la valeur de y3 est =", y3)
y4 = x4*K4
print ("la valeur de y4 est =", y4)
L = F-V
print ("la valeur de L est =", L)