print("Calculator")
operator=input("What operator do you wanna run? (+,-,*,/,%) :")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

if operator=="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="*":
    result=num1-num2
elif operator=="*":
    result=num1-num2
elif operator=="/":
    result=num1/num2
elif operator=="%":
    result=num1%num2
else:
    print("Invalid")
print(f"The value of {num1} {operator} {num2} is {round(result,2)}")
