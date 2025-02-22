def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
fact=factorial(5)

print(fact)

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

f=sum(5)
print(f)

print('....'.join(map(str, range(10))))
num=[123456789]
alpha=['abcdefghi']
for tuple in zip(alpha,num):
    print(tuple)