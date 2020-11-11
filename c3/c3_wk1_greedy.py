import numpy as np
import pandas as pd

x = []
with open('jobs.txt') as f:
    for line in f:
        x.append(line.split())

nums = int(x[0][0])

weights = []
lens = []
for i in range(nums):
    weights.append(x[i+1][0])
    lens.append(x[i+1][1])
weights = np.array(list(map(int, weights)))
lens = np.array(list(map(int, lens)))
orders1 = weights - lens
orders2 = weights/ lens
d = {'weight': weights, 'length': lens, 'order1': orders1, 'order2': orders2}
df = pd.DataFrame(data = d)

df1 = df.sort_values(by = ['order1', 'weight'], ascending= False)
df1['completion_time'] = df1['length'].expanding().sum()
ans1 = (df1['weight']* df1['completion_time']).sum()
print(int(ans1))

df2 = df.sort_values(by = ['order2', 'weight'], ascending= False)
df2['completion_time'] = df2['length'].expanding().sum()
ans2 = (df2['weight']* df2['completion_time']).sum()
print(int(ans2))

