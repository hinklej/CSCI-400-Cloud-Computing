import mincemeat

# CLIENT #
# mincemeat.py -l -p changeme

file = open('medium.txt','r')
data = list(file)
file.close()

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    for number in v.split():	#word -> number
      number = number.strip()
      yield number, 1
      

def reducefn(k, vs):
    count = sum(vs)
    summation = int(k) * count
    return count, summation

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []

for k in results.keys():
  resultlist.append((k,results[k]))
  
resultlist = sorted(resultlist, key=lambda a: a[1])

print resultlist
