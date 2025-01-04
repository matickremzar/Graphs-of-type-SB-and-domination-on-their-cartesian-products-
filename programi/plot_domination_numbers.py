import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

data = []
with open("../podatki/sb_cartesian_products_dominating_numbers_below_9.txt", "r") as F:
    for line in F:
        g1, g2, d = line.rstrip().split()
        data.append(int(d))

bins = np.arange(5, 13)

print(Counter(data))

fig, axs = plt.subplots()

axs.hist(data, bins=bins)
plt.xticks(bins[:-1])

plt.show()
