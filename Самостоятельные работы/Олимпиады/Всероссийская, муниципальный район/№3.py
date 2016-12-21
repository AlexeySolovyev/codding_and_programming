n = int(input())

a = [['?' for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        v = min(abs(i - j), abs(n - 1 - i - j))
        a[i][j] = chr(ord('a') + v % 26)

print("\n".join(["".join(x) for x in a]))
