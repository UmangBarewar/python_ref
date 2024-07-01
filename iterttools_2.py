from itertools import groupby 
def greater_than_3(x):
    return x>3
a=[1,2,3,4,5,6,7]
group_obj=groupby(a,key=greater_than_3)
for key,value in group_obj:
    print(key,list(value))

person=[{'name':'Umang','age':21},{'name':'Aishwarya','age':20},{'name':'Rutuja','age':21},{'name':'Vivek','age':21},{'name':'Akshit','age':21},{'name':'Vineet','age':20}]
group_objj=groupby(person,key=lambda x:x['age'])
for key,value in group_objj:
    print(key,list(value))
