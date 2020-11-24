data = []
with open('knapsack.txt') as f:
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

#################
A = [[None]* (knapsack_size + 1) for i in range(num_items + 1)]
A[0] = [0]* (knapsack_size + 1)

for i in range(1, num_items+1):
    for x in range(0, knapsack_size+1):
        A[i][x] = A[i-1][x]

        if x >= weights[i]:
            case2 = A[i-1][x- weights[i]] + values[i]
            A[i][x] = A[i-1][x] if A[i-1][x] > case2 else case2

print(A[num_items][knapsack_size])