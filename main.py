from Array.array import List

from Array.array import Tuple

from Array.array import Dict

from Array.array import Set

llist = List()
ttuple = Tuple()
ddict = Dict()
sset = Set()

a = [1, 2, 3, 4]

b = (1, 2, 3, 4)

c = {"name": "angappanmuthu", "class": "mca"}

d = {1, 2, 3, 4}

e = {1, 2, 5, 6}

print(llist.append(a, 5))

print(ttuple.max(b))

print(ddict.get(c, 'name'))

print(sset.difference(d, e))
