import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

data = []
with open("../podatki/sb_cartesian_products_dominating_numbers_upper_sampled.txt", "r") as F:
    for line in F:
        g1, g2, d = line.rstrip().split()
        data.append(int(d))

bins = np.arange(min(data), max(data)+1)

print(Counter(data))

fig, axs = plt.subplots()

axs.hist(data, bins=bins)
plt.xticks(bins)

plt.show()
