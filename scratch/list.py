'''
l1 = [1, 2, 7, 3, 4, 5, 6, 7]
l2 = [3, 7, 6, 8]

l2set = set(l2)
l3 = [x for x in l1 if x not in l2set]

print(l3)
'''
'''
l = [1,2,2,3,4] 

sl = [2, 3]

[x for x in [l[n:n + 2] for n in range(0, len(l))[::2]] if x != sl]

print(l)
'''

'''
a = [1,2,2,3,4] 
b = [2, 3]
c = [i for i in a if not i in b or b.remove(i)]

print(c)

# counter verison is much faster
'''

# THIS IS WHAT WORKS AND IS COOL
class BaseItem:

    name = None

    def __init__(self):
        self.__name = self.name

    def __eq__(self, other):
        return self.__name == other

    def __hash__(self):
        return id(self.__name)

    def __repr__(self):
        return f"'{self.__name}'"


class Sword(BaseItem):

    name = "swordName"


class Bow(BaseItem):

    name = "bowName"


class Axe(BaseItem):

    name = "axeName"

inventory = [Sword(), Bow(), Axe(), Sword()]
select = ["bowName", "axeName", "swordName", "bowName", "break?"]
test = []

for item in select:
    if item in inventory:
        test.append(item)
        inventory.remove(item)

print(inventory)
print(test)

# casting lists into sets and getting difference between them

#print(result)  # output {'swordName', 'bowName'}



'''
from math import ceil

def repeat_list_1(values, n):
    repeated = values * ceil(n / len(values))
    return repeated[:n]

values = ['a', 'b', 'c', 1]
n = 4

print(repeat_list_1(values, n))
'''

#for i, j in zip():
'''
from itertools import cycle


values = ['a', 'b', 'c', 1]
n = 10

pool = cycle(values)

for item, limit in zip(pool, range(n)):
    print(item)

# not completely native
'''
'''
values = ['a', 'b', 'c', 1]

def circular():
    while True:
        for connection in values:
            yield connection

n = 10

for item, limit in zip(circular(), range(n)):
    print(item)
'''
'''
values = ['a', 'b', 'c', 1]
n = 10

def circular():
    while True:
        for connection in values:
            yield connection


def repeat_list_2(values, n):
    values_cycler = circular()
    repeated = [next(values_cycler) for _ in range(n)]
    return repeated

print(repeat_list_2(values, n))

#for item, limit in zip(circular(), range(n)):
#    print(item)
'''