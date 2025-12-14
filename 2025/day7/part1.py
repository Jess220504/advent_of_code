with open("2025/day7/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
startPos = 0
beams = []

for i in range(len(lines[0])):
    if lines[0][i] == "S":
        startPos = i
        beams.append(i)

for i in range(1, len(lines)):
    new_beams = []
    for j in range(len(lines[i])):
        for k in range(len(beams)):
            if j == beams[k]:
                if lines[i][j] == ".":
                    lines[i] = lines[i][:j] + "|" + lines[i][j + 1:]
                    new_beams.append(j)
                elif lines[i][j] == "^":
                    lines[i] = lines[i][:j - 1] + "|^|" + lines[i][j + 2:]
                    res += 1
                    new_beams.append(j - 1)
                    new_beams.append(j + 1)
    beams = new_beams[:]

print(res)