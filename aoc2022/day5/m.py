D = [l.strip() for l in open('input.txt')]

for d in D:
    pass

with open("input.txt") as f:
    l = []
    for line in f:
        line = line.strip()
        l.append(line)

print(l)