# Represent the combination of cities with bitmask 
import math

f = open('tsp.txt', 'r')
num_cities = f.readline()
locations = []
location = f.readline()
while location:
    x, y = location.split()
    locations.append((float(x), float(y)))
    location = f.readline()
f.close()

##############
def bitmasks(n,m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield (1 << (n-1)) + x
            for x in bitmasks(n-1,m):
                yield x
        else:
            yield 0
    else:
        yield (1 << n) - 1
 
def index(bit):
    return bit - only_first_city

def split(word):
    return [char for char in word]

def idx_after_remove_cityj(combination, cityj):
    copy = combination.copy()
    copy[cityj - 1] = '0' if copy[cityj - 1] == '1' else '1' 
    res = int(''.join(copy), 2)
    return index(res)

def distance(city1, city2):
    city1_x, city1_y = locations[city1 - 1]
    city2_x, city2_y = locations[city2 - 1]
    return math.sqrt((city1_x - city2_x)**2 + (city1_y - city2_y)**2)

num_cities = 25
only_first_city = 16777216 #   int 16777216 = bit 1000000000000000000000000
all_cities = 33554431      #   int 33554431 = bit 1111111111111111111111111
inifinity = 100000000000000
A = [[inifinity]* (num_cities + 1) for i in range(all_cities - only_first_city + 1)]
A[index(only_first_city)][1] = 0

for m in range(2, num_cities+1):
    print(str(m) + '/' + str(num_cities))
    for bit in bitmasks(num_cities, m):
        if bit < only_first_city:
            continue
        combination_idx = index(bit)
        combination = split('{:025b}'.format(bit))
        location = 1  
        # j won't be the first city
        js = []
        ks = [1]
        for city in combination[1:]: 
            location += 1
            if city == '1':
                js.append(location)
                ks.append(location)
        
        for j in js:
            combination_idx_remove_j = idx_after_remove_cityj(combination, j)
            for k in ks:
                if k != j:
                    choice = A[combination_idx_remove_j][k] + distance(k, j)
                    A[combination_idx][j] = choice if choice < A[combination_idx][j] else  A[combination_idx][j]

results = []
for j in range(2, num_cities + 1):
    res = A[index(all_cities)][j] + distance(j, 1)
    results.append(res)
    print(res)

print(min(results))