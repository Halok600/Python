#Collections : Counter, namedTuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccccccccc"
my_counter = Counter(a)
print(my_counter.values())
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

from collections import namedtuple

#easy to create lightweight object
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x)
print(pt.y)
print(pt)

#Ordered Dict
from collections import OrderedDict
#Just Like Regular dictionary they just remember the order items were inserted

ordered_dict = OrderedDict() #can use normal dict also because after pyhton 3.7 it remembers

ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)


#DefaultDict
from collections import defaultdict
#defaultdict is also similar to normal dict container with only difference that it will have default values for keys that have not been set yet
d = defaultdict(list) #can place list int float
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d['a'])
print(d['b'])
print(d['e']) #default value

#deque
from collections import deque
#double ended queue and it can be used to add and remove elements from both ends
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(3) # add element to first position
d.pop() #remove last element
print(d)
d.popleft() #remove first element from queue
print(d)
d.clear()
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([3,2,1])
print(d)
#rotate
d.rotate(2) #for right rotate
print(d)
#for left rotate
d.rotate(-1)
print(d)