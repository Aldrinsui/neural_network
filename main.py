import sys

lines = [line.strip() for line in sys.stdin if line.strip()]

pred = [
    float(v) for v in lines[0].replace("PRED","").strip().split(',')
]

true =[
    int(v) for v in lines[1].replace("TRUE","").strip().split(',')
]

k = int(
    lines[2].replace("K","").strip()
)

correct = 0

for i in range(len(true)):
    row = pred[i *k : (1+i)* k ]
    pred_class = row.index(max(row))
    if pred_class == true[i]:
        correct += 1

accuracy = correct/len(true)

print(f"{accuracy:.4f}")