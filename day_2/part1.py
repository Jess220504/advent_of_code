with open("Day2/doc.txt", "r") as file:
    lines = file.readlines()
lines = lines[0].split(",")
res = 0

for l in lines:
    for i in range(int(l.split("-")[0]), int(l.split("-")[1])+1):
        if len(str(i))%2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:len(str(i))]:
                res += i
                
print(res)