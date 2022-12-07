from collections import defaultdict
DIR_MAX_SIZE = 100000
TOTAL_SIZE = 70000000
NEEDED_SIZE = 30000000

D = [l.strip() for l in open('input.txt')]

pwd = []
sizes = defaultdict(int)
for d in D:
    # print(d)
    l = d.split()
    if l[0] == "dir" or l[1] == "ls":
        continue
    elif l[1] == "cd":
        if l[2] == "..":
            pwd.pop()
        else:
            pwd.append(l[2])
    else:
        for i in range(1, len(pwd) + 1):
            sizes["/".join(pwd[:i])] += int(l[0])

    # print(pwd)
    print(sizes)

print(sum(v for v in sizes.values() if v <= DIR_MAX_SIZE))
print(min(v for v in sizes.values() if TOTAL_SIZE -
          sizes["/"] + v >= NEEDED_SIZE))
