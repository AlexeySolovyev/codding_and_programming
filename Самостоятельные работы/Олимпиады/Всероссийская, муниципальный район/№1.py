k = str(input())
beauty = 0

while k.startswith("0"):
    k = list(k)
    k.remove("0")
    k = str(k)
    k = ''.join(filter(lambda x: x.isdigit(), k))
while k.endswith("0"):
    k = list(k)
    k.pop()
    k = str(k)
    k = ''.join(filter(lambda x: x.isdigit(), k))

for s in k:
    i = s.find("0")
    if i > -1:
        beauty += 1
print(beauty)
