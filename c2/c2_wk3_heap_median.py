import heapq

X = []

with open('Median.txt') as f:
    for line in f:
        X.append(int(line))

#print(len(X))

negSmallHalf = []
largeHalf = []
heapq.heapify(negSmallHalf)
heapq.heapify(largeHalf)

medians = []

for i in range(10000):
    # originally even, become odd after introducing new Xi
    if i%2 == 0:
        if i == 0:
            median = X[i]
            heapq.heappush(largeHalf, X[i])
            small_more = False
        else:
            smallest_in_large = heapq.nsmallest(1, largeHalf)[0]
            if X[i] <= smallest_in_large:
                neg_X_i = - X[i]
                heapq.heappush(negSmallHalf, neg_X_i)
                small_more = True
                median = - heapq.nsmallest(1, negSmallHalf)[0]
            else:
                heapq.heappush(largeHalf, X[i])
                small_more = False
                median = heapq.nsmallest(1, largeHalf)[0]
    # originally odd (size_l > size_s), become even after introducing new Xi
    else:
        if small_more == True:
            largest_in_small = - heapq.nsmallest(1, negSmallHalf)[0]
            if X[i] >= largest_in_small:
                heapq.heappush(largeHalf, X[i])
            else:
                heapq.heappop(negSmallHalf)
                heapq.heappush(largeHalf, largest_in_small)
                heapq.heappush(negSmallHalf, -X[i])
        else:
            smallest_in_large = heapq.nsmallest(1, largeHalf)[0]
            if X[i] <= smallest_in_large:
                heapq.heappush(negSmallHalf, - X[i])
            else:
                neg_smallest_in_large = - heapq.heappop(largeHalf)
                heapq.heappush(negSmallHalf, neg_smallest_in_large)
                heapq.heappush(largeHalf, X[i])
        median = abs(heapq.nsmallest(1, negSmallHalf)[0])

    medians.append(median)

ans = sum(medians)%10000
print(ans)