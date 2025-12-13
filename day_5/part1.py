with open("Day5/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
ranges = []
nums = []

for i in range(len(lines)):
    line = lines[i][:-1].split("-")
    if len(line) == 2:
        ranges.append([int(line[0]), int(line[1])])
    else:
        if line[0] != "":
            nums.append(int(line[0]))

for n in nums:
    i = 0
    not_found = True
    while not_found and i < len(ranges):
        if n in range(ranges[i][0], ranges[i][1] + 1):
            res += 1
            not_found = False
        i += 1

print(res)