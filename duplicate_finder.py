import os
import sys

path = sys.argv[1]

files_list = []

for _, _, files in os.walk(path):  #  (pathname, [subdirectory], [files])
    for filename in files:  
        files_list.append(filename)


print(files_list)
dict={}
for i in files_list:
    count = files_list.count(i)
    duplicate_list=[]
    while count>1:
        duplicate_list.append(i)
        count-=1
    dict.update({i:duplicate_list})
    
# print(dict)



