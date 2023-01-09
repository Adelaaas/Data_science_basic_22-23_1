
# чтение списка чисел
n = []
for element in input().split():
    n.append(int(element))
    
#1 квадраты
n1 = [  x**2 for x in n ]
print(n1)

#2 целая часть от деления на 4
n2 = [  x//4 for x in n ]
print(n2)

#3 только нечётные элементы 
n3 = [  x for x in n if x%2 == 1 ]
print(n3)

#4 Список, состоящий из чисел, которые если больше 0, то умножаются на 2, если меньше 0, то делятся на 2.
n4 = [  x*2  if x > 0 else x//2 for x in n]

print(n4)

#5 Список, состоящий из выражений [n[i], n[i]_next], где n[i] - элемент списка n, n[i]_next - следующее значение этого элемента (например, [1,2],
n5 = [ x if n.index(x)%2 == 0 else x+1 for x in n ]#?
print (n5)

#6 только на позициях %n5
n6 = [x for x in n if n.index(x)%5 == 0]
print(n6)