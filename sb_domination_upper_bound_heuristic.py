from collections import Counter
d = []
with open("sb_graphs_domination_numbers.txt", "r") as F:
    for line in F:
        d.append(int(line.rstrip()))

d.sort()
d = d[::-1]
print(d[:100])
print(Counter(d))
