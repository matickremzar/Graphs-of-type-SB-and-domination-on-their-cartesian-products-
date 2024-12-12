from sage.all import *

g = Graph("ITm|~z}~g")

prod = g.cartesian_product(g)

cart = prod.dominating_sets()

for s in cart:
    print(len(s))
