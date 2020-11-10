file = open("2sum.txt", 'r')
data = file.readlines()
data = list(map(int, data))

h = {}
n = 100001 # number of buckets

# initiate hash table 
for i in range(n):
    h[i] = []

# put all data into the hash table
for i in range(len(data)):
    if data[i] not in h[data[i]%n]:
        h[data[i]%n] += [data[i]]

tot = 0
r = 0

for t in range(-10000,10001):
    if t%100 == 0:
        print("round:", r)
        r += 1
    for x in data:
        y = t - x
        if x == y:
            continue 
        if y in h[y%n]:
            tot += 1 
            break
        
print(tot)