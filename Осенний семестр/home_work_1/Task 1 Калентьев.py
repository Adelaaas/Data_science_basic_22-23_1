l1=list(input())
l2=list(input())
otvet = []
for element in l1:
    if element in l2:
        continue
    else:
        otvet.append(element)
        
print(otvet)