def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    if show:
        for c in range(n, 0, -1):
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        print(f)
    return f
print (fatorial(5, show=True))