import mincemeat
import sys
from itertools import product
from string import ascii_lowercase
import hashlib


# CLIENT #
# mincemeat.py -l -p changeme


if len(sys.argv) < 2:
    print "Give me a string in the command line"
    sys.exit(1)

given = sys.argv[1]

data = [1, 2, 3]

numbers = '0123456789'

keywords = [''.join(i) for i in product(ascii_lowercase + numbers, repeat = 4)]

#print keywords

datasource = dict(enumerate(data))

hexor = str(hashlib.md5('cats').hexdigest())[:5]
print hexor

#firstFive = hexor[:5]
#print firstFive

def mapfn(k, v):
    print k, v
    yield 'count', 1
    
def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

resultlist = []

results = s.run_server(password="changeme")

for k in results.keys():
        resultlist.append((k,results[k]))

print resultlist
