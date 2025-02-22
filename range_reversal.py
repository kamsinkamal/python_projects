count = int((input("Enter the number ")))
while count>0:
    print('*'*count)
    count-=1
print()
n=int(input("Enter n: "))
for i in range(10,0,-1):
    print('*'*i)
for i in reversed(range(10)):
    print('*'*i)

n=int(input("enter the num: "))
count=1
while count<=n:
    print('*'*count)
    count+=1