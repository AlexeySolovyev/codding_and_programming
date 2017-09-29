print("--------------------------------------------------------------------------------")
print("                                    Задание №7                                  ")
print("--------------------------------------------------------------------------------\n")

things, i, m_case, m_back  = [], 0, 0, 0
s = int(input())
n = int(input())
while i < n:
    x = int(input())
    things.append(x)
    i+=1
for m_thing in things:
    if m_back + m_thing < s:
        m_back += m_thing
    else:
        m_case += m_thing
if m_back != 0:
    print(m_back)
if m_case != 0:
    print(m_case)

input()
