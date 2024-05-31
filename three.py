# N1
# for i in range(10):
#     print(i)

# N2
# def find_longest_word(str) :
#     words = str.split()
#     longest = ""

#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     return longest

# print(find_longest_word("Hello, World"))

# N3
# def evens(nums):
#     for i in range(nums):
#         if i % 2 == 0 :
#             print(i)

# evens(20) 

# N4
# def greetings(num):
#     for i in range(num):
#         print("Hello")

# greetings(4)

# N5
# def sum(num):
#     total = 0
#     for i in range(num+1):
#         total+=i

#     return total

# print(sum(4))

# N7
# secret_num = 4
# user_num = int(input("Enter number: "))

# while user_num != secret_num :
#     user_num = int(input("Guess again: "))
    
# print("Congrats!")

# N8
# def grades(grade):
#     if grade > 90 and grade <=100 :
#         return "A"
#     elif grade <= 90 and grade > 80 :
#         return "B"
#     elif grade <= 80 and grade > 70 :
#         return "C"
#     elif grade <= 70 and grade > 60 :
#         return "D"
#     else :
#         return "F"
    
# print(grades(100))

# N9
# password = "Pa$$word"
# user_guess = input("Enter password: ")

# while user_guess != password :
#     user_guess = input("Guess again: ")
    
# print("Congrats!")

# N10
# def sum(x,y):
#     return f"The sum of {x} and {y} is {x+y}"

# print(sum(4,5))

# N11
# def counter(str,letter):
#     count = 0

#     for i in range(len(str)):
#         if(str[i] == letter):
#             count += 1

#     return count

# print(counter("bitcamp", "b"))