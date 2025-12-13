with open("day4/doc.txt", "r") as file:
    lines = file.readlines()
res = 0

def positions_to_check(h, w, max_h, max_w):
    r = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if h + i >= 0 and h + i <= max_h:
                if w + j >= 0 and w + j <= max_w:
                    if (i == 0 and j == 0) == False:
                        r.append([h + i, w + j])
    return r

for i in range(len(lines)):
    for j in range(len(lines[i][:-1])):
        if lines[i][j] == "@":
            count = 0
            for l in positions_to_check(i, j, len(lines) - 1, len(lines[i][:-1]) - 1):
                if lines[l[0]][l[1]] == "@":
                    count += 1
            if count < 4:
                res += 1
                
print(res)