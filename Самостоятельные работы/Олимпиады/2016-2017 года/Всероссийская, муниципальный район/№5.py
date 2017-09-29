def intria(n, a):
    k = 1
    diag = 1
    while k < a:
        a -= k
        k += 1
        diag += 1
    return a, diag - a + 1

def intriafast(n, a):
    l = 0
    r = n + 1
    while l + 1 < r:
        m = (l + r) // 2
        if m * (m + 1) // 2 < a:
            l = m 
        else:
            r = m
    a = a - l * (l + 1) // 2    
    return a, r - a + 1

def inrevtria(n, a):
    k = n
    diag = 1
    while k < a:
        a -= k
        k -= 1
        diag += 1
    return a + diag - 1, a + 1

def inrevtriafast(n, a):
    l = 0
    r = n + 1
    while l + 1 < r:
        m = (l + r) // 2
        if (n + n - m + 1) * m // 2 < a:
            l = m
        else:   
            r = m
    a = a - (n + n - l + 1) * l // 2

    return a + r - 1, - a + 1

def findsmallr(r, c, a):
    if a <= r * (r + 1) // 2:
        return intriafast(r, a)
    else:
        a -= r * (r + 1) // 2
        dcnt = c - r - 1
        if a <= dcnt * r:
            diag = (a - 1) // r + 1
            row = (a - 1) % r + 1
            return row, r + diag - row + 1
        else:
            a -= dcnt * r
            v = inrevtriafast(r, a)
            v = v[0], v[1] + dcnt + r + 1
            return v

def findsmallc(r, c, a):
    if a <= c * (c + 1) // 2:
        return intriafast(c, a)
    else:
        a -= c * (c + 1) // 2
        dcnt = r - c - 1
        if a <= dcnt * c:
            diag = (a - 1) // c + 1
            col = (a - 1) % c + 1
            return diag + col, c - col + 1
        else:
            a -= dcnt * c
            v = inrevtriafast(c, a)
            v = v[0] + dcnt + 1, c + v[1]
            return v

def findeq(r, a):
    if a <= r * (r + 1) // 2:
        return intriafast(r, a)
    else:
        a -= r * (r + 1) // 2
        v = inrevtriafast(r - 1, a)
        v = v[0] + 1, v[1] + r
        return v

def findfast(r, c, a):
    if r < c:
        return findsmallr(r, c, a)
    elif r > c:
        return findsmallc(r, c, a)
    else:
        return findeq(r, a)

def prepare(r, c):
    x = 0
    y = 0
    a = [[0] * c for i in range(r)]
    for i in range(r * c):
        a[x][y] = i + 1
        x += 1
        y -= 1
        if y < 0 or x >= r:
            found = False
            for tx in range(r):
                for ty in range(c):
                    if a[tx][ty] == 0:
                        x, y = tx, ty
                        found = True
                        break
                if found: 
                    break
    return a

def findslow(ar, a):
    for x in range(len(ar)):
        for y in range(len(ar[x])):
            if ar[x][y] == a:
                return x + 1, y + 1
    return -1, -1

def stress():
    for r in range(1, 21):
        for c in range(1, 21):
            ar = prepare(r, c)
            for a in range(1, r * c + 1):
                stupd = findslow(ar, a)
                smart = findfast(r, c, a)
                if stupd != smart:
                    print(a)

r, c, q = map(int, input().split())
qq = map(int, input().split())

for a in qq:
    x, y = findfast(r, c, a)
    print(x, y)