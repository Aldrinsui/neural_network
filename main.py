import sys
import math

lines = [line.strip() for line in sys.stdin if line.strip()]

for line in lines:
    x = float(line)

    s = 1 / (1 + math.exp(-x))

    derivative = s * (1 - s)

    print(f"{derivative:.4f}")