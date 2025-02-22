string = 'abcdefghijsjf2435464'
print(string[::-1]) # reverse the string because '-' indicates reverse direction, '1' indicates the step
print(string[::1])   # here start and end is not defined but step is defined 
print(string[1::])   # here 0th index character is left out
print()
print(string[::2]) # skips every second chracter
print(string[::-2]) # reverses and skips every second character from the end, '-2' denotes the reverse direction and step
print(string[10:5:-2])

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,]
print(my_list[::-1])
print(my_list[10:5:-2])
print(my_list[2:10:3])
print(my_list[::2])

# for i in string:
    # print(i,i, sep='==')
    # print(i,i ,end='%%')
    # print(i,i, sep='==')

# for i in range(9,-11,-1):
#     print(i,end=',')
# for i in string[5:5]:
#     print(i,end=',')

# negative indexing in slicing
text = "Python"
print(text[-4:-1])  # Output: "tho" (indices -4 to -1)

# With step
nums = [10, 20, 30, 40, 50]
print(nums[::2])  # Output: [10, 30, 50] (skips every second element)

# Negative step for reverse
print(nums[::-1])  # Output: [50, 40, 30, 20, 10] (reversed list)

