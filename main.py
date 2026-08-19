import sys
import math 

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    x_csv,w_csv,b= line.split(";")

    x = [float(v) for v in x_csv.split(",")]
    w = [float(v) for v in w_csv.split(",")]
    b = float(b)

    z = sum(wi * xi for wi , xi in zip(w,x))+b

    sigmoid = 1/(1+math.exp(-z))

    print(f"{sigmoid:.4f}")
