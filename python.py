#adding two no.
def add():
    a=int(input())
    b=int(input())
    s=a+b
    print(s)

#reverse only two digit number
def reverse():
    rev=0
    sum=0
    n=int(input())
    if(9<n<100):
        while(n > 0):
            rem = n % 10
            rev = rev * 10 + rem  #sum=sum+rem
            n = n // 10
        print(rev)
    else:
        print("invalid input")

#sum of digits
def sum_of_digit():
    n=int(input())
    if(999<n<10000):
        temp=0
        for i in str(n):
            temp=temp+int(i)
        print(temp)
    else:
        print("invalid")

def fun():
    a,b=10,5
    s=a+b
    d=a-b
    return s,d
if __name__=="__main__":
    # add()
    # reverse()
    #sum_of_digit()
    x=fun()
    print(x,type(x))
