import numpy

def nearest(a, b):
    n = a[0]
    m = (a[0][0]-b[0])**2+(a[0][1]-b[1])**2+(a[0][2]-b[2])**2
    for i in a:
        if (i[0]-b[0])**2+(i[1]-b[1])**2+(i[2]-b[2])**2 < m:
            n = i
            m = (i[0]-b[0])**2+(i[1]-b[1])**2+(i[2]-b[2])**2
    return n

a = numpy.array([[1, 4, 6], [2, 5, 7], [9, 2, 5], [7, 6, 1]])

print(nearest(a, numpy.array([1, 5, 8])))
