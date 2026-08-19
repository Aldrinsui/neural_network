import sys
import math 

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    x = float(line)

    sigmoid = 1/(1+math.exp(-x))

    print(f"{sigmoid:.4f}")
