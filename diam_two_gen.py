from sage.all import *
import time


start = time.time()
with open("diam_two_graphs.txt", "a") as F:
    for i in range(1, 11):
        for g in graphs.nauty_geng(f"{i} -c"):
            if g.diameter() == 2:
                F.write(str(g.to_dictionary()) + "\n")

end = time.time()
diff = round(end-start, 2)
print("Done! Took ", diff, " seconds to run.")
