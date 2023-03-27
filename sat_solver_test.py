from pycryptosat import Solver
from random_cnf_generator import Generator

g = Generator(5, 10, 3)
s = Solver()
s.add_clauses(g.get_cnf())
sat, solution = s.solve()
print(sat)
print(solution)





