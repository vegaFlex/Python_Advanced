numbers = [int(num) for num in input().split()]
target_num = int(input())

unique_pairs = set()
iterations = 0

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        a = numbers[i]
        b = numbers[j]
        if a + b == target_num:
            unique_pairs.add((a, b))
            print(f"{a} + {b} = {target_num}")
        iterations += 1

print(f"Iterations done: {iterations}")

for pair in unique_pairs:
    print(pair)
