score1 = {
    "A": 1,  # ROCK
    "B": 2,  # PAPER
    "C": 3,  # SCISSORS
    "X": 1,  # ROCK
    "Y": 2,  # PAPER
    "Z": 3,  # SCISSORS
}

lut1 = {
    # 0: LOOSE, 3: DRAW, 6: WIN
    # m    o    r
    ("X", "A"): 3,
    ("X", "B"): 0,
    ("X", "C"): 6,
    ("Y", "A"): 6,
    ("Y", "B"): 3,
    ("Y", "C"): 0,
    ("Z", "A"): 0,
    ("Z", "B"): 6,
    ("Z", "C"): 3,
}

score2 = {"X": 0, "Y": 3, "Z": 6}  # LOOSE  # DRAW  # WIN

lut2 = {
    # r    o    m
    ("X", "A"): 3,
    ("X", "B"): 1,
    ("X", "C"): 2,
    ("Y", "A"): 1,
    ("Y", "B"): 2,
    ("Y", "C"): 3,
    ("Z", "A"): 2,
    ("Z", "B"): 3,
    ("Z", "C"): 1,
}


with open("input.txt") as f:
    r1 = 0
    r2 = 0
    for line in f:
        o, m = line.strip().split(" ")
        r1 += score1[m] + lut1[(m, o)]
        r2 += score2[m] + lut2[(m, o)]

print(r1)
print(r2)
