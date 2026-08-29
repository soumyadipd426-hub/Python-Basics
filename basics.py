#print("Hii")

#Strings
#Name="Soumyadip"
#Address="Rayasandra"

#integers
#roll=32
#marks=89

#print(f"{Name} got {marks} in total")
#print(f"He lives in {Address}")

#float 
#gpa = 8.5

#print(f"his gpa is {gpa}")

#boolean

#is_student=True
#if is_student:
 #   print("He is a student")
#else:
 #   print("He is not a student")

#typecasting
#roll=float(roll)

#print(roll)
#print(type(roll))

#Name=bool(Name)
#print(Name)

#input

#Name=input("Enter your name:")
#age=int(input("Enter your age:"))
#print(f"Hello {Name}! \nYou are {age} year old")

#string methods

#username=input("Enter Your Username:")

#if len(username)>12:
    #print("Username can't be more than 12 Characters!")
#elif not username.find(" ")== -1:
#    print("Username can't contain spaces!")
#elif not username.isalpha():
#    print("Username can't contain numbers!")
#else:
#    print(f"Welcome {username}")

#while loop

age=int(input("Enter your age:"))

while age<0:
    print("Age cant be negative!")
    age=int(input("Enter your age:"))
print(f"You are {age} year old")

num=int(input("Enter a number between 1 - 10 : "))

while num<1 or num>10:
    print(f"{num} is not valid")
    num=int(input("Enter a number between 1 - 10 : "))
print(f"Your number is {num}")
    