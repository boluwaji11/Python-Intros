

words = ['Python', 'C++', 'coding']
string1 = "I'm just checking if you remember your coding project! #Pythong @Baylor"
snt_list = string1.split()
cnt = 0
for i in words:
    if snt_list.count(i)>0:
        cnt+=snt_list.count(i)
        print(i)
print(cnt)



# password = 'ILOVEPYTHON'
# if password.isalpha():
#     print('Invalid, must contain one number.')
# elif password.isdigit():
#     print('Invalid, must have one non-numeric character.')
# elif password.isupper():
#     print('Invalid, cannot be all uppercase characters.')
# else:
#     print('Your password is secure!')

# my_string = '03,07,2018'
# list_strip = my_string.split(',')

# print(list_strip)

# i = 3
# pattern = 'z' * 5 * i
# print(pattern)

# special = '0123456789'
# some_nums = special[0:10:2]
# print(some_nums)

# A = [1,2,3]
# B = [4,5,6]
# C = []

# for i in range(len(A)):
#     C.append(B[i])

# print(C)

# B = [1,2,3,4]
# B[4] = 10

# print(B)

# A = [1,2*3]
# A = A * 3

# print(A)

# A = [1,2,3]
# del(A[-1])
# print(A)