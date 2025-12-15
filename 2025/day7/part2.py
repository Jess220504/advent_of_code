with open("2025/day7/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
startPos = 0
beams = []

for i in range(len(lines[0]) - 1):
    if lines[0][i] == "S":
        startPos = i
        beams.append([i, 1])
    else:
        beams.append([i, 0])

for i in range(1, len(lines)):
    new_beams = beams[:]
    mem = []
    for j in range(len(beams)):
        if lines[i][j] == ".":
            if lines[i][j - 1] == "^":
                new_beams[j][1] += beams[j - 1][1]
            if lines[i][j + 1] == "^":
                new_beams[j][1] += beams[j + 1][1]
        elif lines[i][j] == "^":
            mem.append(j)
    for k in range(len(mem)):
        
        new_beams[mem[k]][1] = 0
    beams = new_beams[:]

for i in range(len(beams)):
    res += beams[i][1]

print(res)