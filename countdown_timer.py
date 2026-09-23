import time
print("Timer!")

t=int(input("Enter the time in seconds: "))

for i in range (t,0,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)%60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    

print("Time is up!")