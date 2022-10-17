import numpy

a = numpy.array([1, 2, 3, 4, 5, 6])
b = []

b.append(a[0])
for i in range(1, len(a)):
    b.append(0)
    b.append(0)
    b.append(0)
    b.append(a[i])

print(numpy.array(b))
