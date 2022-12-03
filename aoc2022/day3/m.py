from string import ascii_lowercase, ascii_uppercase

p = {c: i for i, c in enumerate(ascii_lowercase + ascii_uppercase, 1)}

D = [l.strip() for l in open("input.txt")]
s1 = 0
for d in D:
    assert len(d) % 2 == 0
    i = len(d) // 2
    c1, c2 = d[:i], d[i:]
    c, = set(c1) & set(c2)
    s1 += p[c]

s2 = 0
for i in range(0, len(D), 3):
    c, = set(D[i]) & set(D[i + 1]) & set(D[i + 2])
    s2 += p[c]

print(s1)
print(s2)
