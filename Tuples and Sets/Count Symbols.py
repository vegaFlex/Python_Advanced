text = input()
occurrences = {}

for chr in text:
    if chr not in occurrences:
        occurrences[chr] = 0
    occurrences[chr] += 1

for k, v in sorted(occurrences.items()):
    print(f"{k}: {v} time/s")

