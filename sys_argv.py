# Python program to demonstrate
# sys.argv


import sys 
import os

# os.path.abspath()  takes only one positional argumnets
# os.path.abspath() gives the absolute path i.e. C:\\
# os.path.relpath() gives the relative path i.e. from the current working directory
print("This is the name of the program:", os.path.abspath(sys.argv[0]),type(sys.argv[0]), os.path.relpath(sys.argv[1]),os.path.abspath(sys.argv[1]), sep='\n')

print("Argument List:", sys.argv, str(sys.argv),type(sys.argv), type(str(sys.argv)),sep='\n')  

for i in str(sys.argv):
    print(i)


