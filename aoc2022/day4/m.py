import re
D = [l.strip() for l in open('input.txt')]

a1 = 0
a2 = 0
for d in D:
    s1, e1, s2, e2 = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", d).groups()
    s1 = {n for n in range(int(s1), int(e1) + 1)}
    s2 = {n for n in range(int(s2), int(e2) + 1)}
    if s1 <= s2 or s2 <= s1:
        a1+=1
    if s1 & s2:
        a2+=1
print(a1)
print(a2)
