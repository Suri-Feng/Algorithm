
f = open('2sat6.txt', 'r')
num_clauses = f.readline()
num_clauses = int(num_clauses)

literals1 = []
literals2 = []
literal = f.readline()
while literal:
    literal1, literal2 = literal.split()
    literal1, literal2 = int(literal1), int(literal2)
    literals1.append(literal1)
    literals2.append(literal2)
    literal = f.readline()

def popItems(myList, item):
    try: 
        while True: 
            idx = myList.index(item)
            literals1.pop(idx)
            literals2.pop(idx)   
    except (ValueError):
        pass

################## do reduction first ###################
############# redution is extremely slow ################
deleted = []
original_num_clauses = num_clauses
while True:
    for i in range(1, original_num_clauses + 1):  
        #if i %5000 == 0:
        #    print (i)   
        if i in deleted:
            continue  
        neg_i = -i
        if ((i in literals1 or i in literals2) and (neg_i  not in literals1 ) and (neg_i not in literals2)) or \
             ((neg_i in literals1 or neg_i in literals2) and (i not in literals1) and (i not in literals2)) :
            deleted.append(i)
            popItems(literals1, i)
            popItems(literals2, i)
            popItems(literals1, neg_i)
            popItems(literals2, neg_i)
                        
    new_num_clauses = len(literals1)
    print(new_num_clauses)
    if new_num_clauses == num_clauses:
        break
    else:
        num_clauses = new_num_clauses

print(num_clauses)
print(literals1)
print(literals2)

####### Papadimitriou's randomized local search #########

import random
import math 

variables = []
for i in range(num_clauses):
    if abs(literals1[i]) not in variables:
        variables.append(abs(literals1[i]))
    if abs(literals2[i]) not in variables:
        variables.append(abs(literals2[i]))
num_varibales = len(variables)

for i in range(int(math.log(num_clauses, 2))):
    # choose random initial assignment 
    status_dict = {}
    num_zeros = random.randint(0, num_varibales)
    status = [0]* num_zeros + [1]*(num_varibales - num_zeros)
    random.shuffle(status)
    #print(status)
    for j in range(num_varibales):
        status_dict[variables[j]] = False if status[j] == 0 else True 
        status_dict[-variables[j]] = True if status[j] == 0 else False
    #print(status_dict)
    for k in range(2*num_clauses**2):
        false_clauses = []
        for c in range(num_clauses):
            status = status_dict[literals1[c]] or status_dict[literals2[c]]
            if status == False:
                false_clauses.append(c)
        if false_clauses == []:
            print(status_dict)
            raise Exception('satisfiable!')
        else:
            c = random.choice(false_clauses)
            var1 = literals1[c]
            var2 = literals2[c]
            var = random.choice([var1, var2])
            status_dict[var] = False if status_dict[var] == True else True
            status_dict[- var] = False if status_dict[-var] == True else True
            #print(status_dict)

print('unsatisfiable!')