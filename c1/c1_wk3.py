from statistics import median 

aaa = []
length = 0
with open('QuickSort.txt') as f:
    for line in f:
        length += 1 
        aaa.append(int(line)) 

comparisions = 0
  
def quick_sort(a_list):
    ans =  quick_sort_helper(a_list, 0, len(a_list) - 1, 0)
    return ans

# exchange the last with the first
def exchange(a_list, l, r):
    a_list[l], a_list[r] = a_list[r], a_list[l]
    return a_list

# exchange the median with the first 
def exchange2(a_list, l, r):
    m = (r - l)//2 + l
    first = a_list[l]
    last = a_list[r]
    middle = a_list[m]
    candidates = [first, middle, last]
    md = median(candidates)
    if middle == md:
        a_list[l], a_list[m] = a_list[m], a_list[l]
    if last == md:
        a_list[l], a_list[r] = a_list[r], a_list[l]
    return a_list


def quick_sort_helper(a_list, first, last, comparision):
    if first >= last:
        return comparision
    a_list = exchange2(a_list, first, last)
    split_point = partition(a_list, first, last)
    f_cmp = quick_sort_helper(a_list, first, split_point - 1, comparision)
    s_cmp = quick_sort_helper(a_list, split_point + 1, last, comparision)
    comparision += f_cmp + s_cmp + last - first
    return comparision


def partition(a_list, l, r):
    p = a_list[l]
    i = l + 1
    for j in range(l +1 , r + 1):
        if a_list[j] < p:
            temp = a_list[j]
            a_list[j] = a_list[i]
            a_list[i] = temp
            i += 1
    temp = a_list[l]
    a_list[l] = a_list[i - 1]
    a_list[i - 1] = temp
    return i - 1




'''
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
what = quick_sort(a_list)
print(a_list)
print(what)

'''
count = quick_sort(aaa)
print(aaa)
print(count)



