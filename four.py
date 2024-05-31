# N1
# def sum(list):
#     total = 0

#     for num in list:
#         total+=num

#     return total

# print(sum([1,2,3]))

# N2
# def middle(list):
#     middle = 0
#     for num in list :
#         middle +=num

#     return middle/len(list)

# print(middle([1,2,3]))

# N3
# def sort_list(list):
#     return sorted(list)

# print(sort_list([2,4,7,1]))

# N4
# def greater_num(list):
#     return sorted(list)[len(list)-1]

# print(greater_num([8,4,1,7,2]))

# N5
# def smallest_num(list):
#     return sorted(list)[0]

# print(smallest_num([3,5,1,7,8]))

# N6
# def find_element(list,element):
#     if element in list :
#         return "Found"
#     else :
#         return "Could not find the element"
    
# print(find_element(["Hello",2, "World", 4,],"Hello"))

# N7
# def remove_element(list):
#     list.pop()
#     return list

# print(remove_element([1,2,3,4,5]))

# N8
# def element_count(list,user_element):
#     count = 0
#     for element in list :
#         if element == user_element :
#             count+=1

#     return count

# print(element_count([5,2,4,1,4,6,4],4))

# N9
# def sum_of_even(list):
#     count = 0
#     for element in list :
#         if element%2 == 0:
#             count += element

#     return count

# print(sum_of_even([1,2,3,4]))

# N10
# def second_greatest(list):
#     return sorted(list)[len(list)-2]

# print(second_greatest([3,1,5,6,7]))

# N11
# def lists_equal(list1,list2):
#     if len(list1) != len(list2):
#         return False
    
#     for i in range(len(list1)):
#         if list1[i] != list2[i]:
#             return False
        
#     return True

# print(lists_equal([1,2,3],[1,2,4]))

# N12
# def sum(list1, list2):
#     return list(set(list1 + list2))

# print(sum([1,2,3],[4,2,6]))

# N13
# def by_alphabet(list):
#     return sorted(list)

# print(by_alphabet(["d","s","a"]))

# N14
# def common_elements(*lists):
#     base_list = lists[0]
#     common_elements = []

#     for i in range(len(base_list)) :
#         includes = True
#         for j in range(1,len(lists)) :
#             if base_list[i] not in lists[j] :
#                 includes = False
#                 break

#         if includes :
#             common_elements.append(base_list[i])

    
#     return common_elements

# print(common_elements([1, 2, 3, 2], [2, 3, 4, 2], [4, 5, 3, 2, 1, 6]))

# N15
# car = {
#     'brand': 'mercedes',
#     'model': 'gClass',
#     'year': 2019
# }

# print(car)

# N16
# car = {
#     'brand': 'mercedes',
#     'model': 'gClass',
#     'year': 2019,
#     'start': lambda: 'The car is starting'
# }

# print(car['start']())

# N17
# person = {'name':'Mariam', 'age':16, 'city':'Tbilisi'}
# print(person['age'])

# N18
# person = {'name':'Mariam', 'age':16, 'city':'Tbilisi'}
# person['job'] = 'programming'

# print(person)
