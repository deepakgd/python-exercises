from collections import defaultdict;
a=['1','2','3','2','1','4','5','4','4','3']
res = defaultdict(list)
print(res)
for i in a: 
    res[i].append(i)

print(res.items())
print(sorted(res.items()))

for (k,v) in res.items():
    print(k, v, "length: ",len(v))

print("----OR----")
a=['1','2','3','2','1','4','5','4','4','3']
b = {}
for i in a:
    if(not i in b): b[i] = []
    b[i].append(i)

for (k,v) in b.items():
    print(k,v, "length: ", len(v))