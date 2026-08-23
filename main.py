import sys
import math

lines = [line.strip() for line in sys.stdin if line.strip()]

LR = float(lines[0].replace("LR","").strip())
WEIGHTS=[
    float(v) for v in lines[1].replace("WEIGHTS","").split(',')
]
GRADS=[
    float(v) for v in lines[2].replace("GRADS","").split(',')
]

NEW_WEIGHT =[]

for w,g in zip(WEIGHTS,GRADS):
    phew_weight = w - LR * g
    NEW_WEIGHT.append(phew_weight)

print(",".join(f"{w:.4f}" for w in NEW_WEIGHT))