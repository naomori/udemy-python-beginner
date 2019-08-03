def g_hello():
    yield 'hello 1'
    yield 'hello 2'
    yield 'hello 3'

def g_hello2():
    r = yield 'hello'
    yield r

def g_hello3():
    while True:
        r = yield 'hello'
        yield r

if False:
    for w in g_hello():
        print(w)

elif False:
    g = g_hello()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
elif False:
    g = g_hello2()
    print(next(g))
    print(g.send('plus'))
    print(next(g))
elif True:
    g = g_hello3()
    print(next(g))
    print(g.send('mike'))
    print(next(g))
    print(g.send('nancy'))
else:
    print('bye')
