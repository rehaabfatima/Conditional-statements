num=float(input("Enter number to check:"))

if num>50:
    print("The number is greater than 50")
    if num%2==0:
        print("and it is even too")
    else:
        print("And it is odd too")   
else:
    print("The number is less than 50")         
