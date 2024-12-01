from collections import Counter


l = []
r = []
# sum = 0
# with open('input.txt', 'r') as file:
#     data = file.read().splitlines()
    
#     for entry in data:
#         print(entry)
#         split = entry.split(' ')
#         l.append(int(split[0]))
#         r.append(int(split[3])) 
#     l.sort()
#     r.sort()
#     for entry in range(len(l)):
#         sum += abs(l[entry] - r[entry])

# print(sum)
sim_sum = 0
with open('input.txt', 'r') as file:
    data = file.read().splitlines()
    
    for entry in data:
        print(entry)
        split = entry.split(' ')
        l.append(int(split[0]))
        r.append(int(split[3]))
    for entry in l: 
        c = Counter(r)
        sim_sum += entry * c[entry]
print(sim_sum)
    