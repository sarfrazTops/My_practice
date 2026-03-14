
#()marks = int(input("Enter the marks: "))

#if marks < 0 or marks > 100:
    #print("enter marks between 0 and 100")
#else:
    #if (marks>90 and marks<100):
        #print("A Grade")
    #elif (marks>60 and marks<80):
        #print("B Grade")        
    #else:
        #print("Grade not in the specified range")
#for row in range(5,0,-1):
    #for col in range(1,row+1):
        #print("*",end=" ")
    #print("\n")        

#starcount=1
#for i in range(1,6):
    #for j in range(starcount):
        #print("*",end="")
    #print("")
    #starcount+=1


#starcount = 5
#for i in range(1, 6):
    #for j in range(starcount):
        #print("*", end="")
    #print("")
    #starcount -= 1

#for row in range(1,6):
    #for col in range(1,6-row):
        #print(" ",end="")
    #for col in range(1,row+1):
        #print("*",end="")
    #print("\n")
#for row in range(1,5):
    #for col in range(1,6-row):
        #print(" ",end="")
    #for col in range(1,(2*row-1)+1):
        #print("*",end="")
    #print("\n")


for row in range(1,6):
    for col in range(row,0,-1):
        print(col,end=" ")
    print()






















 
   
