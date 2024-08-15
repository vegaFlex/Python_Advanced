n = int(input())
even = set()
odd = set()

for row in range(1, n+1):
    sum_names_ascii = sum([ord(chr) for chr in input()]) // row

    if sum_names_ascii % 2 == 0:
        even.add(sum_names_ascii)
    elif sum_names_ascii % 2 == 1:
        odd.add(sum_names_ascii)

sum_even = sum(even)
sum_odd = sum(odd)

if sum_even == sum_odd:
    result = odd.union(even)

elif sum_odd > sum_even:
    result = odd.difference(even)

elif sum_even > sum_odd:
    result = odd.symmetric_difference(even)

print(*result, sep=', ')




