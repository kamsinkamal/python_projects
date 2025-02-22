list=['a','b','c','d',]
b=[]
list.append(['e'])
list.append([9,8,7,6])
list.extend([1,2,3,4,5,6])
print(list)

b=['a','a','a','a',]
pop = b.pop(0)
count = b.count(pop)
print(b, pop, count)

str = 'ababababababab'
empty = ''
for i in str:
    if str.index(i)%2!=0:
        c= i.upper()
        empty+=c
    else:
        empty+=i
print([empty, empty.swapcase()])

dict = {'name':'kamal','age':23}
print(dict['name'])

list = []
for i in range(10):
    list +=[i]
print(list)
string = 'malayalam'
empty =''
for i in reversed(string):
    empty+=i
for i in string[2::]:
    print(i)
print(empty, empty==string)
