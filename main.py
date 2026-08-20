import sys
import math 

line = [line.strip() for line in sys.stdin if  line.strip()]

x = [ float(v) for v in line[0].replace("INPUT","").split(",")]
WEIGHTS = [float(v) for v in line[1].replace("WEIGHTS","").split(",")]
BIAS = [float(v) for v in line[2].replace("BIAS","").split(",")]
M,N = map(int,line[3].split()[2:])
output =[]
for i in range(M):
    row = WEIGHTS[i *N:(i+1)*N]
    z = sum(wi * xi for wi , xi in zip(row, x ))
    z += BIAS[i]
    result = 1/(1+math.exp(-z))
    output.append(f"{result:.4f}")

print(",".join(output))
