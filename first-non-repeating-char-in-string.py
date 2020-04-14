#code

from collections import defaultdict

n = int(input())

for i in range(n):
    a, b = int(input()), list(input())
    res = defaultdict(list)
    isPrint = True
    for item in b:
        res[item].append(item)

    for (k,v) in res.items():
        print(k,v, isPrint, len(v))
        if(isPrint == True and len(v) == 1):
	        print(k)
	        isPrint = False
        
        
