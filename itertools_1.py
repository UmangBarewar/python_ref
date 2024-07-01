from itertools import product,permutations,combinations,accumulate
a=[2,3,6]
b=[3,4]
c=[5]
# print(list(product(a,b)))
# print(list(product(a,c,repeat=2)))

perm=permutations(a)
comb=combinations(a,2)
print(list(perm))
print(list(comb))

e=[4,5,6,7]
acc=accumulate(e)
acc_str=str(acc)
print(list(acc))

