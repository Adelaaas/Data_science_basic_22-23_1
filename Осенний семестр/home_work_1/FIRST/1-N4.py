#N4
arr = input().split()

print([int(x) ** 0.5 for x in arr])
print([int(int(x) / 4) for x in arr])
print([int(x) for x in arr if int(x) % 2 == 1])
print([int(x) / 2 if int(x) < 0 else int(x) * 2 for x in arr])
print([[int(x), int(x) + 1] for x in arr])
print([int(arr[i]) for i in range(0, len(arr)) if i % 5 == 0])