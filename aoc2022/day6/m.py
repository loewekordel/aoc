D = open('input.txt').read()

p1 = False
p2 = False
for i in range(len(D)):
    if len(set(D[i:i + 4])) == 4 and not p1:
        print(i + 4)
        p1 = True
    if len(set(D[i:i + 14])) == 14 and not p2:
        print(i + 14)
        p2 = True
    if p1 and p2:
        break
