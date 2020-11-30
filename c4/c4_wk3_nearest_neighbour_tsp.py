import math

f = open('nn.txt', 'r')
num_cities = f.readline()
num_cities = int(num_cities)
locations = {}
location = f.readline()
while location:
    n, x, y = location.split()
    locations[int(n)] = (float(x), float(y))
    location = f.readline()
f.close()

visited = [False]*(num_cities + 1)
visited[0] = True
all_visited = [True]*(num_cities + 1)

visited[1] = True
current = 1
tot_dis = 0

count = 0 
while(visited != all_visited):

    count += 1
    if count%2000 == 0:
        print(count)

    distances_square = {}
    cityc_x, cityc_y = locations[current]
    
    for i in range(num_cities + 1):
        if visited[i] == False:
            city2_x, city2_y = locations[i]
            distances_square[i] = (cityc_x - city2_x)**2 + (cityc_y - city2_y)**2

    next_current = min(distances_square, key = distances_square.get)
    citync_x, citync_y = locations[next_current]
    tot_dis += math.sqrt((cityc_x - citync_x)**2 + (cityc_y - citync_y)**2)
    visited[next_current] = True 
    current = next_current

cityc_x, cityc_y = locations[current]
city1_x, city1_y = locations[1]
tot_dis += math.sqrt((cityc_x - city1_x)**2 + (cityc_y - city1_y)**2)

print(tot_dis)


    
