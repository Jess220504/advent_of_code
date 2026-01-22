with open("2015/day2/doc.txt", "r") as file:
    lines = file.readlines()
res = 0
dim = []

for l in lines:
    splitted_line = l[:-1].split("x")
    new_line = []
    for i in range(len(splitted_line)):
        new_line.append(int(splitted_line[i]))
    dim.append(new_line)

for i in range(len(dim)):
    present = [dim[i][0] * dim[i][1], dim[i][1] * dim[i][2], dim[i][0] * dim[i][2]]
    res += present[0] * 2 + present[1] * 2 + present[2] * 2 + min(present)
    print(dim[i], present, present[0] * 2 + present[1] * 2 + present[2] * 2 + min(present))
        
print(res)