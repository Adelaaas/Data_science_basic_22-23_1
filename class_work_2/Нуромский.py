#задача 6
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x2 = []
for i in range(len(x)):
    if i%2 == 0:
        x2.append(x[i])
    else:
        x2.append(x[(len(x)//2-1-i//2)*2+1])
print(x2)
