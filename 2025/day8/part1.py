with open("2025/day8/doc.txt", "r") as file:
    lines = file.readlines()
MAX_NB_CONNECTIONS = 1000
MAX_LARGEST_BOXES = 3
res = 1

def calculate_distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d += (p1[i] - p2[i]) ** 2
    return d ** 0.5

distances = []

for i in range(len(lines)):
    l = lines[i].split(",")
    for j in range(len(l)):
        l[j] = int(l[j])
    lines[i] = l

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        distances.append([i, j, calculate_distance(lines[i], lines[j])])

distances = sorted(distances, key = lambda x: x[2])
circuits = [[distances[0][0], distances[0][1]]]
nb_connections = 0

i = 0
while nb_connections < MAX_NB_CONNECTIONS:
    count = 0
    j = 0
    condition = True
    while j < len(circuits) and condition:
        if distances[i][0] not in circuits[j] and distances[i][1] not in circuits[j]:
            count += 1
        elif distances[i][0] in circuits[j] and distances[i][1] not in circuits[j]:
            k = 0
            while k < len(circuits) and condition:
                if distances[i][1] in circuits[k]:
                    for ii in range(len(circuits[k])):
                        circuits[j].append(circuits[k][ii])
                        condition = False
                    del circuits[k]
                k += 1
            if condition:
                circuits[j].append(distances[i][1])
        elif distances[i][0] not in circuits[j] and distances[i][1] in circuits[j]:
            k = 0
            while k < len(circuits) and condition:
                if distances[i][0] in circuits[k]:
                    for ii in range(len(circuits[k])):
                        circuits[j].append(circuits[k][ii])
                        condition = False
                    del circuits[k]
                k += 1
            if condition:
                circuits[j].append(distances[i][0])
        j += 1
    if count == len(circuits): 
        circuits.append([distances[i][0], distances[i][1]]) 
    c = 0
    nb_connections += 1
    i += 1 
        
circuits = sorted(circuits, reverse = True, key = lambda x: len(x))

for i in range(min(len(circuits), MAX_LARGEST_BOXES)):
    res *= len(circuits[i])
            
print(res)