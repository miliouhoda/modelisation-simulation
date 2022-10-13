import numpy as np
T = 773.15
P = 197.38
R = 0.082
MATRICE = []
MATRICE.append(['He', 0.03412, 0.0237])
MATRICE.append(['Ne', 0.2107, 0.01709])
MATRICE.append(['O2', 1.36, 0.03183])
MATRICE.append(['N2', 1.39, 0.03913])
MATRICE.append(['CH4', 2.253, 0.04278])
MATRICE.append(['HCl', 3.667, 0.04081])
MATRICE.append(['CO2', 3.592, 0.04267])
MATRICE.append(['NH3', 4.17, 0.03707])
MATRICE.append(['H2O', 5.464, 0.03049])
MATRICE.append(['Cl2', 6.493, 0.05622])
MATRICE.append(['Hg', 8.093, 0.01696])
for MATRICE in MATRICE:
    B = -(P * MATRICE[2] + R * T)
    C = -MATRICE[1] * MATRICE[2]
    coeff = [P, B, MATRICE[1], C]
    sol = np.roots(coeff)
    print("valeur de volume molaire de ", MATRICE[0], " est =", sol[0].real)
