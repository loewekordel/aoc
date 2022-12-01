l = []

with open("input.txt") as f:
    s = []
    for line in f:
        if not line.strip():
            l.append(sum(s))
            s = []
        else:
            s.append(int(line))

l = sorted(l)
print(l)
print(l[-1])
print(sum(l[-3:]))
