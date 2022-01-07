# heading = "Python: An Introduction"

# header, _, subheader = heading.partition(': ')

# print(header)
# print(subheader)

# first, second, third = heading.partition(': ')

# print(first)
# print(second)
# print(third)

# tags = 'python,coding,programming,development'

# tags = tags.split()

# api_data = '5'
# greeting = 'Hi'

# print(greeting.isnumeric())

# product_id = 123 #integerorwholenumber
# sale_price = 14.99 #floatingnumbertype
# tip_percentage = 1/5 #percentage20percent
# new_product = 150

# print(sale_price + new_product)

# print('Addition')
# print(100 + 42)

# print('Subtraction')
# print(100 - 42)

# print('Division')
# print(100 / 42)
# print(100 / 38)

# print('Floor Division')
# print(100 // 42)
# print(100 // 38)

# print('Multiplication')
# print(100 * 42)

# print('Modulus') #RETURNS REMAINDER
# print(100 % 42)

# print('Exponents')
# print(11 ** 2)

#USES PEMDAS (Please Excuse My      Dear Aunt Sally)
#            (Par()  Exp**  Multi*  Div/ Add+ Sub-)
# calculation = 8 + 2 * 5 - (9+2) ** 2
# print(calculation)

# total = 100
# total = total + 10
# total -= 10 #Subtraction
# total += 10 #Addition
# total *= 2 #Multiplication
# total /= 20 #Division
# total **= 2 #Integer (Squared)
# total //= 2 #Floor Division
# total %=2 #Modulus (Is it an Even or Odd Number? 0=Even 1=Odd)
# print(total)

# from decimal import Decimal

# product_cost = Decimal(88.40)
# commission_rate = Decimal(0.08)
# qty = 450


# product_cost += (commission_rate * product_cost)
# print(product_cost * qty) 
#WITHOUT DECIMAL 42962.4 
#WITH DECIMAL LIBRARY 42962.40000000000282883716451

# from decimal import Decimal

# product_cost = Decimal(88.80)
# commission_rate = Decimal(0.08)
# qty = 450
# print(int(product_cost))
# print(float(qty))
# print(Decimal(product_cost))
# print(complex(commission_rate))

# from decimal import ROUND_HALF_UP
# import math

# loss = -20.25
# product_cost = 89.99

# print(abs(loss))
# print(math.floor(product_cost))
# print(math.ceil(product_cost))
# print(abs(math.floor(loss)))
# print(round(product_cost))
# print(math.sqrt(product_cost))
# print(math.pow(5, 2))
# print(5 ** 2)

# manual_exponent(2, 3)
#>8

# manual_exponent(10,2)
#>100

# import math
# from functools import reduce

# def manual_exponent(num, exp):
#     counter = exp - 1
#     total = num

#     while counter > 0:
#         total *= num
#         counter -= 1
    
#     return total

#ANOTHER WAY TO DO IT USING REDUCE:
# def manual_exponent(num, exp):
#     computed_list = [num] * exp
#     return (reduce(lambda total, element: total * element, computed_list))

# print(manual_exponent(2, 3))
# print(manual_exponent(10, 2))


# """
# User Database Query
# Kristine
# Tiffany
# jordan
# """

# users = ['Kristine', 'Tiffany', 'Jordan']
# print(users)

# users.insert(0, 'Trenton')
# print(users)

# users.append('Joseph')
# print(users)

# print([users[2]])

# users[4] = 'Brayden'

# print(users)

# users = ['Trenton', 'Joseph', 'Jude', 'Koda']
# print(users)

# users.remove('Joseph')
# print(users)

# popped_user = users.pop()
# print(popped_user)
# print(users)

# del users[0]
# print(users)

# users = ['Trenton', 'Joseph', 'Jude', 'Koda']
# ids = [1, 2, 3, 4]

# mixed_list = [42, 10.3, 'Altuve', users]
# user_list = mixed_list.pop()

# nested_lists = [[123], [234], [345]]

# print(users)
# print(mixed_list)
# print(users)

# tags = ['python', 'development', 'tutorial', 'code']
# len = length (calls in number of items WITHOUT COUNTING 0)
# Positions still start at 0. EXAMPLE Code is in position 3.

# number_of_tags = len(tags)
# print(number_of_tags)

# last_item = tags[-1]
# print(last_item)

# index_of_last_item = tags.index(last_item)
# print(index_of_last_item)

# tags = ['python', 'development', 'tutorials', 'code']

# print(tags)

# tags.sort() #This is alphabetical

# print(tags)

# tags.sort(reverse=True) #runs alphabetical in reverse order

# print(tags)

# totals = [234, 1, 543, 2345]

# totals.sort(reverse=True)

# print(totals)

# uri = 'https://www.google.com/search?q='
# tags = ['python', 'development', 'tutorial']
# formatted_tags = '+'.join(tags) #join is used on strings
# query_uri = f'{uri}{formatted_tags}'

# print(query_uri)

# tags = ['python', 'development', 'tutorials', 'code']
# tag_range = tags[:]

# print(tag_range)

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# sorted_list = sorted(sale_prices, reverse=True)

# print(sorted_list)
# print(sale_prices)


# import math
# """
# Tools:
# - math library
# - sorted function
# - list slicing
# - computations
# """

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# sorted_list = sorted(sale_prices)
# num_of_sales = len(sorted_list)
# half_slice = math.floor(num_of_sales/2)
# first_sales_items = sorted_list[:half_slice]
# last_sales_items = sorted_list[-(half_slice):]
# median = sorted_list[half_slice:(half_slice + 1)]

# print(sorted_list)
# print(num_of_sales)
# print(first_sales_items)
# print(last_sales_items)
# print(median)

# tags = [
#     'Trenton',
#     'Joseph',
#     'Koda',
#     'Kai',
#     'Jude',
#     'Nova',
#     'August',
# ]

# print(tags[1:7:2])

# slice_obj = slice(1, 7, 2)

# print(slice_obj.start)
# print(slice_obj.stop)
# print(slice_obj.step)

# print(tags[slice_obj])

# tags = ['Trenton', 'Kai','Koda', 'Joseph', 'Jude', 'AuGUSt', 'Nova']
# new_tags = tags + ['Family']

# # tags[-1] = 'Family'

# # tags.extend('Family') #SEPERATES EACH CHARACTER TO A STRING
# # new_tags = tags.extend(['Family']) #USE BRACKETS TO MAKE IT A SINGLE STRING
# # print(new_tags) #CAN NOT STORE IN EXTEND MUST MAKE NEW DEFINITION

# print(tags)
# print(new_tags)

# import numpy as np

# weights = {
#     'Winning': 1,
#     'Losing': 1000
# }

# def lottery_num():
#     container_list = []

#     for (name, weight) in weights.items():
#         #loop x number of times
#         for _ in range(weight):
#             container_list.append(name)
#     return container_list

# CREATING Dictionary
# players = {
#         "ss": "Correa",
#         "2b": "Altuve",
#         "3b": "Bregman",
#         "DH": "Gattis",
#         "OF": "Springer",
# }

# second_base = players['2b']

# print(second_base)

# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ['Price', 'Betts'],
# }

# featured_team = teams.get('yankees', 'No featured team')

# print(featured_team)

# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }

# player_names = list(players.copy().values())


# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# removed_team = teams.pop('yankees', 'No team found by that name')
# del teams['astros']
# print(teams.get('mets', 'No team found by that name'))

# print(teams)
# print(removed_team)


# sales = {
#   'google': 20,
#   'twitter': 10,  
#   'facebook': 42,
#   'offline': 12,
# }

# print('g ' + sales['google'] * '$')
# print('t ' + sales['twitter'] * '$')
# print('f ' + sales['facebook'] * '$')
# print('o ' + sales['offline'] * '$')


# List: [] MUTABLE
# Dictionary: {}
# Tuple: () IMMUTABLE

# post = ('Python Basics', 'Intro guide to python', 'Some python content')

# title, sub_heading, content = post



# # title = post[0]
# # sub_heading = post[1]
# # content = post[2]

# print(title)
# print(sub_heading)
# print(content)

# post = ('Python Basics', 'Intro guide to python', 'Some python content')
# print(id(post))

# post += ('Published',)
# print(id(post))

# title, sub_heading, content, status = post



# print(title, sub_heading, content, status)

# post = ('Python Basics', 'Intro guide to python', 'Some python content')

# tags = ['python', 'coding', 'tutorial']

# post += (tags,)

# print(post[-1][1])

# post = ('Python Basics', 'Intro guide to python', 'Some python content', 'published')
#Removing Elements from End!
# post = post[:-1]
#Removing Elements from Start!
# post = post[1:]
#Removing Specific Element: NOT BEST PRACTICE!
#Changes Tuple to List. Has to be changed back to Tuple AFTER!
# post = list(post)
# post.remove('published')
# post = tuple(post)

# print(post)

# priority_index = {
#   (1, 'premier'): [1, 34, 12],
#   (1, 'mvp'): [84, 22, 24],
#   (2, 'standard'): [93, 81, 3],
# }
# print(list(priority_index.keys()))

# positions = ['2b', '3b', 'ss', 'duh']
# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# scoreboard = zip(positions, players)

# print(list(scoreboard))

# tags = {
#     'python',
#     'coding',
#     'tutorials'
# }
# #How To Query a SET
# query_one = 'python' in tags
# query_two = 'ruby' in tags

# print(query_one)
# print(query_two)

# tags_one = {
#     'python',
#     'coding',
#     'tutorials',
#     'coding'
# }

# tags_two = {
#     'ruby',
#     'coding',
#     'tutorials',
#     'development'
# }
#Merge Tags Removed Duplicates
# merged_tags = tags_one | tags_two
# print(merged_tags)

#Tags in tags 1 but not in tags 2
# exclusive_to_tag_one = tags_one - tags_two
# exclusive_to_tag_two = tags_two - tags_one
# print(exclusive_to_tag_one)
# print(exclusive_to_tag_two)

#Tags in both 1 & 2 tags
# common_tags = tags_one & tags_two
# print(common_tags)

# def heading_generator(title, heading_type):
#     return f'<h{heading_type}>{title}</h{heading_type}>'

# print(heading_generator('Hi there', 3))
# print(heading_generator('What up', 1))

# dogs = {
#     'YLA': 'Nova',
#     'GES': 'Kai',
#     'CGI': 'Jude',
#     'CLA': 'Gus',
#     'AUS': 'Koda'
# }

# for breed, dog in dogs.items():
#     print('Breed Code: ', breed)
#     print('Name: ', dog)

# alphabet = 'abcdefg'

# for letter in alphabet:
#     print(letter)

# def loop_over_string():
#     name = 'Trenton'
#     for char in name:
#         print(char)
#     return name

# print(loop_over_string())

# def loop_over_range():
#     for num in range(1,11):
#         print(num)

# print(loop_over_range())

# usernames = [
#     'tdenton',
#     'jdenton',
#     'cperugini',
#     'smeier',
# ]

# for username in usernames:
#     if username == 'cperugini':
#         print(f'Sorry, {username}, you are not allowed.')
#         continue
#     else:
#         print(f'{username} is allowed.')
# for username in usernames:
#         if username == 'cperugini':
#             print(f'{username} was found at index {usernames.index(username)}')
#             break
#         print(username)

# def loop_and_break():
#     vegetables = ['onion', 'broccoli', 'apple', 'spinich']
#     for vegetable in vegetables:
#         if vegetable != 'apple':
#             print(vegetable)
#         else:
#             print(f'{vegetable} is not a vegetable')
#             break
# loop_and_break()






#HERE IS THE COMPLETED BUT SAYS ERROR


# def loop_using_while():
#     dog_house = ['Nova', 'Kai', 'Jude', 'Gus', 'Koda',] 
#     counter = 0
#     while counter <= 4:
#         counter +=1
#         print(dog_house.pop())

#     return [dog_house, counter]

# loop_using_while()



# def loop_over_list():
#     numbers = [1,2,3,4,5,6]
#     result = []    
#     for number in numbers:
#         result.append(number + 1)
#         print(result)
    
#     return result
# loop_over_list()


# legacy_customers = ['Alice', 'Bob']
# new_customers = ['Tiffany', 'Kristine']

# raw_db = [legacy_customers, new_customers]

# for legacy_customer in legacy_customers:
#     new_customers.append(legacy_customer)

# print(new_customers)

# num_list = range(1, 11)
# cubed_nums = []

# for num in num_list:
#   cubed_nums.append(num ** 3)

# cubed_nums = [num ** 3 for num in num_list]

# print(cubed_nums)

# even_numbers = []

# for num in num_list:
#   if num % 2 == 0:
#     even_numbers.append(num)

# num_list = range(1, 11)
# even_numbers = [num for num in num_list if num % 2 == 0]

# print(even_numbers)



# def list_comprehension():
#     numbers = [1,2,3,4,5,6]
#     result = [number + 1 for number in numbers]
#     print(result)
#     return result
# list_comprehension()

# answer = False

# if answer == False:
#   answer = True
#   print(answer)


# def loop_using_while():
#     dog_house = ['Nova', 'Kai', 'Jude', 'Gus']
#     counter = 0
#     while counter != 4:
#         counter += 1 
#     for dog in dog_house:
#         print(dog)
#     return [dog_house, counter]
# loop_using_while()

# language = "python"

# language_check = True if language == "python" else False
# print(language_check)

# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

# def value_in_string():
#     sentence = 'Python is the best!'
#     word = 'Python'
    
#     if word.lower() in sentence.lower():
#       print('The word is in the sentence')
#     else:
#       print('The word is not in the sentence')
# value_in_string()

# username = 'jonsnow'
# email = 'jon@snow.com'
# password = 'thenorth'

# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#     print('Access Granted')
# else:
#     print('Access Denied')


# def compound_conditional(number):
#     if number in range(1, 101):
#         print("Success!")
#     else:
#         print("Failure...")
# compound_conditional(100)

#FUNCTION(S)

# def sum_two_numbers(num_one, num_two):
#     num_one = num_one + num_two
#     # print(num_one)
#     return num_one
# sum_two_numbers(1, 5)

# def greeting(persons_name):
#   def name():
#     return f'{persons_name}'

#   print("Hello,", persons_name)

# greeting('Jordan')




# def counter(initial_count = 0):
#     initial_count += 1
#     return initial_count
# print(counter())
# counter()



# def function(first_name, last_name):
#     greeting = (f'Hello, {first_name} {last_name}.'

# function()


# first_name = 'Jordan'
# last_name = 'Hudgens'

# def function(first_name, last_name):
#     greeting = print(f'Hello, {first_name} {last_name}')

#     return greeting

# function("Jordan", "Hudgens")

# def greeting(name):
#     greeting = f'Hello, {name}'
#     print(greeting)
#     return greeting
# greeting('Jordan')

# def named_arguments_practice(sequence):
#     sequence(first = '1', second = '2', third = '3', fourth = '4', fifth = '5')
# named_arguments_practice()

# def greeting(*args):
#   print('Hi ' + ' '.join(args))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')


# def greeting(*names):
#   print('Hi ' + ' '.join(names))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')


# def greeting(time_of_day, *args):
#   print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


# greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
# greeting('Morning', 'Tiffany', 'Hudgens')


# def greeting(time_of_day, *args, **kwargs):
#     print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}!")

#     if kwargs:
#         print('Your tasks for the day are:')
#         for key, val in kwargs.items():
#             print(f"{key} => {val}")

# greeting('Morning',
#          'Trenton', 'Denton',
#          firt = 'Empty Dishwasher',
#          second = 'Take dogs outside',
#          third = 'Do the laundry')

# full_name = lambda first, last: f'{first} {last}'

# def greeting(name):
#     print(f'Hi there {name}')

# greeting(full_name('Trenton', 'Denton'))

# def lambda_practice(name):
#     greeting = lambda firstname: f'{firstname}'
#     print(f'Hi, {name}')
#     return greeting
# lambda_practice('Trenton')



#FIZZBUZZ TEST

# def fizbuzz(x):
#     for i in range(1, x+1): 
#         if i % 3 == 0 and i %5 == 0:
#             print('FizzBuzz')
#             continue
#         elif i % 3 == 0:
#             print('Fizz')
#             continue
#         elif i % 5 == 0:
#             print('Buzz')
#             continue
#         else:
#             print(i)
# fizbuzz(100)

# for i in range(100):print('Fizz'*(i%3>1)+(i%5>3)*'Buzz'or i+1)
# import numpy as np

# def converter(num):
#     counter = num * 4
#     num = counter / 4
#     print(counter) 
# converter(15)

#CLASSES OVERVIEW

# class Invoice:
#     def greeting(self):
#         return 'Hi There'
    
# inv_one = Invoice()
# print(inv_one.greeting())

# class Garage:
#     def open_door(self):
#         return 'The door opens'
    
# home = Garage()




# class Invoice:
#     def __init__(self, client, total):
#         self.client = client
#         self.total = total

#     def formatter(self):
#         return f'{self.client} owes: ${self.total}'

# google = Invoice('Google', 100)
# snapchat = Invoice('Snapchat', 200)

# print(google.formatter())
# print(snapchat.formatter())

# class Garage:
#     def __init__(self, size):
#         self.size = size
#         return

#     def open_door(self):
#         return "The door opens"
    
# home = Garage(2)


#CAN OVERRIDE VALUE WITH SETTER.
# class Invoice:
#     def __init__(self, client, total):
#         self.client = client
#         self.total = total

#     def formatter(self):
#         return f'{self.client} owes: ${self.total}'

# google = Invoice('Google', 100)
# print(google.client)

# google.client = 'Yahoo' #OVERRIDE FUNCTION
# print(google.client)
# Starter code


# class Garage:
#   def __init__(self, size):
#     self.size = size
#     self.cars = []

#   def open_door(self):
#     return "The door opens"
    
# home = Garage(2)
# home.size = 0
# get_cars = home.cars

# print(home.size)

# class Garage:
#   def __init__(self, size):
#     #   Protect the size attribute
#     self._size = size
#     self.cars = []

#   @property
#   def size(self):
#     return self._size

#   def open_door(self):
#     return "The door opens"





#DUNDER = DOUBLE UNDERSCORES
#HAS TO DO WITH PRIVATE/PROTECTED METHODS.
# class Invoice:
#   def __str__(self):
#     return "This is the invoice class!"


# inv = Invoice()
# print(str(inv))

# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def __str__(self):
#     return f"Invoice from {self.client} for {self.total}"


# inv = Invoice('Google', 500)
# print(str(inv))

# class Invoice:
#   def __init__(self, client, total):
#     self.client = client
#     self.total = total

#   def __str__(self):
#     return f"Invoice from {self.client} for {self.total}"

#   def __repr__(self):
#     return f"Invoice({self.client}, {self.total})"


# inv = Invoice('Google', 500)
# print(str(inv))
# print(repr(inv))

# class Website:
#   def __init__(self, title):
#     self.title = title

# ws = Website('My Website Title')
# print(ws.__dict__)

# ws_two = Website('Second Title')
# print(ws_two.__dict__)







# #POLYMORPHIC FUNCTIONS IN PYTHON. RENDER. HTML.
# class Html:
#     def __init__(self, content):
#         self.content = content
    
#     def render(self):
#         raise NotImplementedError('Subclass must implement render method')
        
# class Heading(Html):
#     def render(self):
#         return f'<h1>{self.content}</h1>'

# class Div(Html):
#     def render(self):
#         return f'<div>{self.content}</div>'

# tags = [ #first set
#     Div('Some Content'),
#     Heading('Some Big Heading'),
#     Div('AnotherDiv')
#     ]

# div_one = Div('Some Content')
# heading = Heading('Some Big Heading')
# div_two = Div('Another div') #second set

# def html_render(tag_object):
#     print(tag_object.render()) 
# for tag in tags: #first set
#     print(tag.render()) 

# html_render(div_one)
# html_render(div_two)
# html_render(heading) #second setup



#BUILD A FILE WITHIN PYTHON
# file_builder =open("logger.txt", "w+")
# file_builder.write("Hey, I'm in a file!")
# file_builder.close()

# file_builder = open("loggers.txt", "w+")

# for i in range (100):
#     file_builder.write (f"I'm on line {i + 1}\n")
# file_builder.close()



#FN MATCH AND SEARCHING FILES ETC
# import fnmatch
# from fnmatch import fnmatchcase
# import os

# def list_files():
#     for file in os.listdir('.'):
#         if fnmatch.fnmatch(file, '*.txt'):
#             print('Text files:', file)

#         if fnmatch.fnmatch(file, '*.rb'):
#             print('Ruby files:', file)

#         if fnmatch.fnmatch(file, '*.yml'):
#             print('Yaml files:', file)

#         if fnmatch.fnmatch(file, '*.py'):
#             print('Python files:', file)


# list_files()

# players = [
#     "Jose Altuve 2B",
#     "Carlos Correa SS",
#     "Alex Bregman 3B",
#     "Scooter Gennett 2B"
# ]

# second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

# print(second_base_players)


#PRETTY PRICE OR TOTAL GENERATOR FOR ECOMMERCE
# def pretty_price(gross_price, extension):
#     if isinstance(extension, int):
#         extension = extension * 0.01
#     return int(gross_price) + extension

# print(pretty_price(3.50, 0.95))
# print(pretty_price(3.50, 95))





# num_list = [1, 2, 3, 4, 5, 6]

# def average(num):
#     sum_num = 0
#     for i in num:
#         sum_num = sum_num + i
    
#     avg = sum_num / len(num)
#     return avg
# print("The average is", average(num_list))

# my_list = {
#     "Kaldr",
#     "Koda",
#     "Gus",
#     "Kai",
#     "Nova"
# }

# def loop_over_list():
#     for name in my_list:
#         print(name)
#     return my_list;

# loop_over_list()


# greeting= lambda name: f'{name}'

# def lambda_practice(name):
#     return f'Hi, {name}'

# print(lambda_practice(greeting('Jordan')))