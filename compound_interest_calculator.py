#a=p(1+r)^t
print("[Compound Interest Calculator]")

principle=float(input("Enter the principle value:"))
rate=float(input("Enter the rate of interest /year:"))
#rate should be 0 to 100
while rate<0 or rate>100:
    print("Rate is invalid!")
    rate=float(input("Enter the rate of interest /year:"))

time=int(input("Enter the Time period in years:"))

final=principle*((1+(rate/100))**time)

compound=final-principle

print(f"The final amount is {final: .2f}\n ")
print(f"The Compound interest is {compound: .2f}")


