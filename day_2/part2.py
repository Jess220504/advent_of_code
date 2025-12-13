with open("Day2/doc.txt", "r") as file:
    lines = file.readlines()
lines = lines[0].split(",")
res = 0

def divisible(n):
    r = []
    for i in range(1, n):
        if n%i == 0:
            r.append(i)
    return r

def split(l, n):
    r = []
    for i in range(0, len(l)//n):
        r.append(l[i*n:(i+1)*n])
    return r

for l in lines:
    last_id = 0
    for i in range(int(l.split("-")[0]), int(l.split("-")[1])+1):
        div = divisible(len(str(i)))
        for j in div:
            splitted_i = split(str(i), j)
            cpt = 0
            for k in range(1, len(splitted_i)):
                if splitted_i[k] == splitted_i[0]:
                    cpt += 1
            if cpt == len(splitted_i) - 1:
                if last_id != i:
                    res += i
                    last_id = i
        
print(res)