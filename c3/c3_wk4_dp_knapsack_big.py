data = []
with open('knapsack_big.txt') as f:
    for line in f:
        data.append(line)

knapsack_size, num_items = data[0].split()
knapsack_size, num_items = int(knapsack_size), int(num_items)

values = [0]
weights = [0]

for i in range(1, num_items + 1):
    value, weight = data[i].split()
    values.append(int(value))
    weights.append(int(weight))

######## to save space, only record down necessary combinations of n and w ########

n_list = [num_items]
w_list = [knapsack_size]
v_dict = {(num_items, knapsack_size): 0}
keys = []

i = 0
while True:
    ni = n_list[i]
    wi = w_list[i] 
    if ni <= 0:
        break
    if (ni - 1, wi) not in v_dict:
        n_list.append(ni - 1)
        w_list.append(wi)
        v_dict[(ni - 1, wi)] = 0
    if wi - weights[ni] >= 0 and (ni, wi - weights[ni]) not in v_dict:      
        n_list.append(ni - 1)
        w_list.append(wi - weights[ni])
        v_dict[(ni - 1, wi - weights[ni])] = 0
    i += 1
    if i % 1000000 == 0:
        print(i)

########################### dp #############################
for i in reversed(range(len(n_list))):
    ni = n_list[i]
    wi = w_list[i]
    if ni == 0:
        continue 
    v_dict[(ni, wi)] = v_dict[(ni -1 , wi)]
    if wi > weights[ni]:
        v_dict[(ni, wi)] = max(v_dict[(ni-1, wi)], v_dict[(ni - 1, wi - weights[ni])] + values[ni] )
    if i % 1000000 == 0:
        print(i)

print(v_dict[num_items, knapsack_size])

