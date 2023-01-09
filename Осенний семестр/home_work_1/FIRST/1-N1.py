#N1
list1 = list(input())
list2 = list(input())

for el in list1:
    if el not in list2:
        print(el, end = ' ')

