def s_hello():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'
    return 'Done'

def g_hello():
    while True:
        r = yield from s_hello()
        yield r

g = g_hello()

for _ in range(8):
    print(next(g))
