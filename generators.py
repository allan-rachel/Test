
def naturals():
    x = 1
    while True:
        yield x
        x = x + 1


print(next(naturals()))
print(next(naturals()))
print(next(naturals()))
print(next(naturals()))
print("-----")
g = naturals()
g2 = naturals()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


print("hi")
print(next(g2))
