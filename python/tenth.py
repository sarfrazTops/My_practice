#(10):-

def factroial(m):
    fact=1
    for i in range(1,m+1):
        fact=fact*i
        print("factorial of",m,"is",fact)
n=int(input("Enter the number "))
factroial(n)
