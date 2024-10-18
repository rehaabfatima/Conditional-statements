height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg:"))

BMI=weight / (height/100)**2

print("Your BMI : ",BMI)

if BMI <= 14.9:
    print("You are under weight")
elif BMI <= 24.5:
    print("You are healthy")    
elif BMI <= 29.9:
    print("You are overweight")    
elif BMI <= 34.9:
    print("You are severely overweight")    
elif BMI <= 39.9:
    print("You are slightly obese")   
else:
    print("You are obese")     
    