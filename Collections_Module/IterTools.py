# itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product
a = [1,2]
b = [3,4]

prod = product(a,b)
print(prod)
print(list(prod))
b = [3]
prod1 = product(a,b, repeat = 2)
print(list(prod1))

#permutations
#return all possible orderings of the input
from itertools import permutations
a =  [1,2,3]
perm = permutations(a)
perm = permutations(a,2)
print("Permutations")
print(list(perm))
perm = permutations(a,2)
print(list(perm))

#combinations
from itertools import combinations, combinations_with_replacement
#make all possible combinations with specified lenght'
a = [1,2,3,4]
comb = combinations(a, 2) #length mandotory
print("COMBINATION") #no repetition
print(list(comb))

comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))


#Accumulate Function

#return accumulated sums or anyother binary func it is given as input

from itertools import accumulate
import operator 
acc = accumulate(a) #by default compute sums
print("ACCUMULATE")
print(list(acc))

acc = accumulate(a, func = operator.mul)
print(list(acc))
a = [1, 2, 5, 3, 2 ]
acc = accumulate(a, func = max)

print(list(acc))
 
print("Groupby")
#groupby
from itertools import groupby
def smaller_than_3(x):
    return x<3
a = [1,2,3,4]
group_obj =  groupby(a,key = lambda x: x<3)#groupby(a, key = smaller_than_3)
print(group_obj)
for key,value in group_obj:
    print(key,list(value)) 

persons = [{'name':'Tim', 'age': 25},{'name':'Dan', 'age': 25},{'name':'Lissa', 'age': 27},{'name':'Claire', 'age': 28}]

group_obj = groupby(persons, key = lambda x: x['age'])

for key,value in group_obj:
    print(key,list(value)) 


#Infinte Iterators
print("INFINITE iterators")
from itertools import count,cycle,repeat

for i in count(10):
    print(i)
    if i==15:
        break

a = [1, 2, 3] 
for i in cycle(a): #Will cycle the list again and again
    print(i)
    if i==3:
        break
for i in repeat(1, 5): # will repeat the value number of time
    print(i)
     

