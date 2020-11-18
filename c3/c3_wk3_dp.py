f  = open('mwis.txt', 'r')
x = f.readlines()
f.close()
num_vertices = int(x[0])
weights = list(map(int, x))
weights[0] = 0

################ dp #################
A = [0]*(num_vertices + 1)
A[0], A[1] = weights[0], weights[1]
for i in range(2, num_vertices + 1): 
    choice2 = A[i-2] + weights[i]
    A[i] = A[i-1] if A[i-1] > choice2 else choice2

########## reconstruction ###########

S = []
i = num_vertices
while i>= 1:
    if A[i-1] >= A[i-2] + weights[i]:
        i -= 1
    else:
        S.append(i) 
        i -= 2

check = [1, 2, 3, 4, 17, 117, 517, 997]
for c in check:
    if c in S:
        print(1)
    else:
        print(0)
