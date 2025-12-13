with open("day6/test.txt", "r") as file:
    lines = file.readlines()
res = 0
new_l = []

for line in lines:
    splitted_line = line.split(" ")
    for i in range(len(splitted_line)):
        if splitted_line[i] != "" and splitted_line[i] != "\n":
            if "\n" in splitted_line[i]:
                new_l.append(splitted_line[i][:-1])
            else:
                new_l.append(splitted_line[i])

print(new_l, len(lines))

for i in range(len(new_l) // len(lines) - 1):
    print("calculs")
