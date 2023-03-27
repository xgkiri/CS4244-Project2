from pycryptosat import Solver
from random_cnf_generator import Generator
import matplotlib.pyplot as plt

n = 150
K = []
for k in range(3, 5):
    R = []
    P = []
    for r_10 in range(2, 100, 2):
        r = r_10 / 10
        R.append(r)
        g = Generator(n, int(r * n), k)
        num_sat = 0
        for i in range(50):
            s = Solver()
            s.add_clauses(g.get_cnf())
            sat, _ = s.solve()
            if sat:
                num_sat += 1
        prop = num_sat / 50
        P.append(prop)
    K.append((R, P))

for i in range(len(K)):
    plt.plot(K[i][0], K[i][1])




