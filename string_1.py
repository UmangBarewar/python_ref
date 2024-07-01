my_string = "Hello how are you"
my_list=  my_string.split(' ')
print(my_list)

# list to string
new_string=' '.join(my_list)
print(new_string)


from timeit import default_timer as timer

# good approach
listt=["a"]*100000
# print(listt)

start= timer()
stringg=""
for _ in listt:
    stringg+=_ 
    
stop=timer()
print(stop-start)

# good approach
start=timer()
stringgg="".join(listt)
stop=timer()
print(stop-start)

    