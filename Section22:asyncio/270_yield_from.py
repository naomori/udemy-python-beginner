def g_hello():
    while True:
        r = yield from 'hello'
        yield r

g = g_hello()
print(next(g))
print(next(g))
