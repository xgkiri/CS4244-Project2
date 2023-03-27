from random_cnf_generator import Generator
from utils import cnf2string
import os
root = "../data"
data_name = "test_data.txt"
g = Generator(10, 15, 3)
CNF = []
for i in range(50):
    CNF.append(cnf2string(g.get_cnf()))
fd = open(os.path.join(root, data_name), "w")
for j in range(len(CNF)):
    fd.write(CNF[j])
fd.close()

