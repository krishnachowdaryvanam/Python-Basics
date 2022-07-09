from functools import reduce

from functools import reduce
num = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda n: n%2 ==0 , num))
double = list(map(lambda n: n+2, evens))
addAll = reduce(lambda a,b: a+b, double)
print(evens)
print(double)
print(addAll)