print("Calculator")
operator=input("What operator do you wanna run? (+,-,*,/,%) :")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))


if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    
    if num2!=0:
        
        if num1!=0:
            result=num1/num2
        else:
            print(f"The value of {num1} {operator} {num2} is 0")
            result=""
    else:
        print(f"The value of {num1} {operator} {num2} is infinity")
        result=""
    
elif operator=="%":
    result=num1%num2
else:
    print("Invalid")
    result=""
if result:
    print(f"The value of {num1} {operator} {num2} is {round(result,2)}")
