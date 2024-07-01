from itertools import accumulate
n=int(input("Enter the number of elements in fibonacci series"))
a=list(range(n))
print(a)
acc=accumulate(a)
print(list(acc))
