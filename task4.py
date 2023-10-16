num = int(input(" enter the no of terms till which you want to print the fibonacci sequence==>"))
def fibonacci(num):

    a=0
    b=1
    print(a,end="|")
    print(b,"|")
    for i in range(1,num+1):
        c=a+b
        a=b
        b=c
        print(c,end="|")
fibonacci(num)        
