numbers = [int(x) for x in input().split()]

pos = 0
neg = 0

for num in numbers:
    if num >= 0:
        pos += num
    else:
        neg += num

print(neg)
print(pos)

if abs(neg) > pos:
    print("The negatives are stronger than the positives")
elif pos > abs(neg):
    print("The positives are stronger than the negatives")