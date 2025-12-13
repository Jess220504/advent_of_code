with open("day1/doc.txt", "r") as file:
    lines = file.readlines()
num = 50
res = 0

for i in range(len(lines)):
    line = lines[i][:-1]
    rotation = int(line[1:])
    if line[0] == "R":
        num += rotation
        while num > 99:
            num -= 100
    if line[0] == "L":
        num -= rotation
        while num < 0:
            num += 100
    if num == 0:
        res += 1
        
print(res)