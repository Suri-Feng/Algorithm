aaa = []
length = 0
with open('IntegerArray.txt') as f:
    for line in f:
        length += 1 
        aaa.append(int(line))
  
# Driver Code 
arr = [1, 20, 6, 4, 5] 
n = len(arr) 

  
def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:int(len(arr)/2)]
        b = arr[int(len(arr)/2):]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
                inversions += (len(a)-i)
        c = c + a[i:]
        c = c + b[j:]

    return c, inversions

_, inversions = mergeSortInversions(aaa)
print("Number of inversions are", 
            inversions)