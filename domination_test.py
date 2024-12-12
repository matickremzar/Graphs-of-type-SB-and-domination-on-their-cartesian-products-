from sage.all import *

g = Graph("EEhw")

prod = g.cartesian_product(g)

s = prod.dominating_set(value_only=True)
print(s)
