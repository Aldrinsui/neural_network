import sys
import math 

lines = [line.strip() for line in sys.stdin if line.strip()]

pred = [float(v) for v  in lines[0].replace("PRED ","").split(",")]
true =[float(v) for v in lines[1].replace("TRUE ","").split(",")]

squared_errors = []

for p,t in zip(pred,true):
    error = p - t
    squared_error = error * error
    squared_errors.append(squared_error)

mse = sum(squared_errors)/len(squared_errors)

print(f"{mse:.4f}")