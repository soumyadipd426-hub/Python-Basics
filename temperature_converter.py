unit=input("Enter the unit of the temperature! (C/F)")
temp=float(input("Enter the temperature: "))

#F=(C×9/5​)+32
if unit=="C":
    F=(temp*(9/5))+32
    print(f"The temp in fahrenheit is {round(F,2)} degree f")
elif unit=="F":
    C=(5/9)*(temp-32)
    print(f"The temp in Celcius is {round(C,2)} degree c")
else :
    print("invalid entry")


