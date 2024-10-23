def fib(n):
    a=0
    b=1
    it=n-2
    print(a)
    print(b)
    while(it):
        c=a+b
        print(c)
        a=b
        b=c
        it-=1
fib(5)
