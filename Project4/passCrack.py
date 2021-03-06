import mincemeat
import sys
from itertools import product
from string import ascii_lowercase
import hashlib

# CLIENT #
# mincemeat.py -l -p changeme

# ONLY WORKS FOR d077f #

       #SEE LINE 33

########################


if len(sys.argv) < 2:
    print "Give me a string in the command line"
    sys.exit(1)

given = sys.argv[1]

numbers = '0123456789'

keywords = []
for n in range(1,5):
    keywords = keywords + [''.join(i) for i in product(ascii_lowercase + numbers, repeat = n)]

datasource = dict(enumerate(keywords))

def mapfn(k, v):
    hexit = str(hashlib.md5(v).hexdigest())[:5]
    if(hexit == 'd077f'):
        yield 'found', v
      
def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []

for k in results.keys():
        resultlist.append((k,results[k]))

print resultlist
