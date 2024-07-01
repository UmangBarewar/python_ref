from collections import Counter
a="aaaaaaaaaabbbbbbcccc"
my_counter=Counter(a)
print(my_counter)
print(my_counter.most_common(2))
print(my_counter.most_common(1)[0][0])
print(my_counter.most_common(1)[0])

print(list(my_counter.elements()))