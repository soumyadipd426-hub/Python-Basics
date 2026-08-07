response=input("Do you wanna buy something?(Y/N):")
if response=="Y":
    item=input("What do you wanna add? ")
    price=float(input("What is the price? "))
    quantity=int(input("How many do u want? "))

    total=price*quantity
    print(f"You have bought {quantity} X {item}/s")
    print(f"Your total is: {total}")    
else:
    print("No worries!")
    