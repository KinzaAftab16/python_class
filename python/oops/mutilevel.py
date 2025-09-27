class one:
    a = 10

class two(one):
    b = 20

class three(two):
    c = 30

o = two()
print(o.a , o.b)

f = three()
print(f.a, f.b, f.c)