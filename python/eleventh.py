if largest(a,b,c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
        else:
            
            if b>=c:
                return b
            else:
                return c
num=int(input("enter the first number"))
num=int(input("enter the 2nd number"))
num=int(input("enter the 3d number"))
largest=largest(num1,num2,num3)
print(largest)


              
