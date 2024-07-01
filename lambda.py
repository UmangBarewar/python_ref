add10=lambda x:x+10
print(add10(5))
mul=lambda x,y:x*y
print(mul(5,10))

#  similar to 
def add10_func(x):
    return x+10
# sorted function
points2D=[(1, 2),(15, 1),(10, 4)]
points2D_sorted = sorted(points2D, key=lambda x:x[1]+x[0])
print(points2D)
print(points2D_sorted)
# map funciton

a=[12,2,34,5]
b=list(map(lambda x:x+2,a))
# this can be done using list comprehension as well/
c=[x+2 for x in a]
print(c)
print(b)

# filter function
d=filter(lambda x:x%2==0,a)
# again this can be done ny list comprehension
e=[x%2==0 for x in a]
f=[x for x in a if x%2==0]
print(f)
print(list(d))
print(e)

# reduce function
from functools import reduce
product_a=reduce(lambda x,y:x*y,a)
print(product_a)

