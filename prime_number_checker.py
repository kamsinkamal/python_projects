a=abs(int(input("Enter the number: ")))
if a==2 or a==3:
    print(f"{a} is a prime number")
elif a<=1 or a%2==0 or a%3==0 or a%5==0:
    print(F"{a} is not a prime number")
else:
    count=2
    while a%count!=0:
        count+=1
    if count==a:
        print(f"{a} is a prime number")
    else:
        print(F"{a} is not a prime number")