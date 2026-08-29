#a=p(1+r)^t
print("[Compound Interest Calculator]")
principle=0
rate=0
time=0

while principle<=0: 
    principle=float(input("Enter the principle value:"))
    if principle<=0:
        print("Invalid")

while rate<=0 or rate>100: 
    rate=float(input("Enter the rate of interest /year:"))
    if rate<=0:
        print("Invalid")
    elif rate>100:
        print("Invalid")

while time<=0: 
    time=int(input("Enter the Time period in years:"))
    if time<=0:
        print("Invalid")

final=principle*((1+(rate/100))**time)

compound=final-principle

print(f"The final amount after {time} Years is {final: .2f}\n ")
print(f"The Compound interest is {compound: .2f}")


