import re
from collections import defaultdict, deque
from copy import deepcopy

D = open('input.txt').read()
stacks = defaultdict(deque)
data, instr = D.split("\n\n")

for d in data.splitlines()[:-1]:
    for i, e in enumerate(d):
        if e == "[":
            stacks[i//4 + 1].appendleft(d[i+1])

stacks = dict(sorted(stacks.items()))
cmds = re.findall(r"move (\d+) from (\d+) to (\d+)", instr)

stacks1 = deepcopy(stacks)
for n, f, t in cmds:
    for i in range(int(n)):
        stacks1[int(t)].append(stacks1[int(f)].pop())

stacks2 = deepcopy(stacks)
for n, f, t in cmds:
    tmp = deque()
    for i in range(int(n)):
        tmp.appendleft(stacks2[int(f)].pop())
    stacks2[int(t)].extend(tmp)

print("".join(v.pop() for v in stacks1.values()))
print("".join(v.pop() for v in stacks2.values()))