import mincemeat
import sys

# CLIENT #
# mincemeat.py -l -p changeme


if len(sys.argv) < 2:
    print "Give me a file in the command line"
    sys.exit(1)

file = open(sys.argv[1],'r')
data = file.readlines()
file.close()

datasource = dict(enumerate(data))

def mapfn(k, v):
    yield 'count', 1
    yield 'sum', int(v)
    yield 'std dev', float(v)**(2.0)
    
def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []

for k in results.keys():
    if(k == 'count'):
        count = results[k]
    elif(k == 'sum'):
        summation = results[k]
    elif(k == 'std dev'):
        squaredsum = results[k]
        
stddev = round(((squaredsum - summation**(2.0)/count)/count)**(1/2.0), 2)

#std dev = sqrt[(B- A^2/N)/N]
for k in results.keys():
    if(k == 'std dev'):
    	resultlist.append((k, stddev))
    else:
        resultlist.append((k,results[k]))

print resultlist
