#N3
pal = input()

i = 0
while i < len(pal) - i - 1:
    if pal[i] != pal[len(pal) - i - 1]:
        print('Не палиндром')
        break

    i += 1