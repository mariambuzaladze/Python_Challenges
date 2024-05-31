# def anagram_checker(str1, str2):
#     return sorted(str1) == sorted(str2)
# print(anagram_checker(input("Write a string: "),input("Write another string: ")))

##################

# print(sorted(input("Write a string: ")) == sorted(input("Write another string: ")))

################
# print((lambda str1, str2: sorted(str1) == sorted(str2))(input("Write a string: "), input("Write another string: ")))


# def prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5)):
#         if num % i == 0:
#             return False
#     return True

# def prime_nums(start, end):
#     for i in range(start, end):
#         if prime(i):
#             return i
        
# print(prime_nums(1,14))


# x = 5 
# y = 3
# # a = x
# # x = y
# # y = a
# x, y = y, x
# print(x, y)