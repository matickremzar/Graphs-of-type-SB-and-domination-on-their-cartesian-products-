import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

data = []
with open("../podatki/sb_cartesian_products_dominating_numbers_below_9.txt", "r") as F:
    for line in F:
        g1, g2, d = line.rstrip().split()
        data.append(int(d))

bins = np.arange(min(data), max(data)+2)

print(Counter(data))

fig, ax = plt.subplots()

ax.hist(data, bins=bins)
plt.xticks(bins)
ax.set_title("Dominacijska števila kartezičnih produktov grafov tipa (SB) z 8 vozlišči ali manj")
plt.yscale("log")
plt.xlabel('Dominacijsko število')
plt.ylabel('Število pojavitev')

plt.show()
