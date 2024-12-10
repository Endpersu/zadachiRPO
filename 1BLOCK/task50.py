import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def perimetr(a, b, c):
    return distance(a, b) + distance(b, c) + distance(c, a)

def area(a, b, c):
    ab = distance(a, b)
    bc = distance(b, c)
    ca = distance(c, a)

    s = (ab + bc + ca) / 2

    return math.sqrt(s * (s - ab) * (s - bc) * (s - ca))

x1, y1 