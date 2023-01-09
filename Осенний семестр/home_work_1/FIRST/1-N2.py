#N2
lst = ['a', 4, 'hello', (1,5), 10, 'b']
for i in range(0, 5, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(lst)