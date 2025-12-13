with open("Day5/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
ranges = []

for i in range(len(lines)):
    line = lines[i][:-1].split("-")
    if len(line) == 2:
        ranges.append([int(line[0]), int(line[1])])

ranges = sorted(ranges, key = lambda x: x[0])
min_num = ranges[0][0]

for i in range(len(ranges)):
    res += 0 if ranges[i][1] - max(ranges[i][0], min_num) + 1 < 0 else ranges[i][1] - max(ranges[i][0], min_num) + 1
    min_num = min_num if (ranges[i][1] + 1) < min_num else ranges[i][1] + 1

print(res)