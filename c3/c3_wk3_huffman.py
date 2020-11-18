import heapq 

f  = open('huffman.txt', 'r')
x = f.readlines()
f.close()
num_symbols = int(x[0])
weights = list(map(int, x[1:]))
weights_dict = {k: [v] for v, k in enumerate(weights)}

depths = [0]*num_symbols
heapq.heapify(weights)


# going to have (num - 1) merges
for i in range(num_symbols - 1):
    weight1 = heapq.heappop(weights)
    weight2 = heapq.heappop(weights)
    symbols = []
    for symbol in weights_dict[weight1]:
        symbols.append(symbol)
        depths[symbol] += 1
    for symbol in weights_dict[weight2]:
        symbols.append(symbol)
        depths[symbol] += 1
    newWeight = weight1 + weight2 
    weights_dict[newWeight] = symbols 
    heapq.heappush(weights, newWeight)
    del weights_dict[weight1]
    del weights_dict[weight2]

print('max: ', max(depths))
print('min: ', min(depths))
