lst= ['a', 4, 'hello', (1,5), 10, 'b']

print(lst)

lst[0],lst[1] = lst[1],lst[0]

lst[2],lst[3] = lst[3],lst[2]

lst[4],lst[5] = lst[5],lst[4]

print(lst)