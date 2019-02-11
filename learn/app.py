#V1     HELLO WORLD
# print("Hello Wolrd")

#V2     PRINT
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

#V3     VARIABLES
# character_name = "Tom"
# character_age = 50
# isMale = True
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")
# character_name = "Mike"
# print("He really liked the name "+ character_name + ", ")
# print("but didn't like being "+ character_age + ". ")

#V4     STRINGS
# phrase = "Pingle Mingle Single"
# print(phrase.upper())
# print(phrase.isupper())
# print(len(phrase))
# print(phrase[5])
# print(phrase.index("in"))
# print(phrase.replace("in","*"))
# print(phrase.replace("\0","*"))

#V5     NUMBERS
# from math import *
# print("--1=" + str(- - 1))
# print("3+4*5=" + str(3+4*5))
# print("10 % 51 = "+ str(10%51))
# my_num = 5
# print("My Num is " + str(my_num))
# print("|-10|="+str(abs(-10)))
# print("3^2=" + str(pow(3,2)))
# print(max(4,6))
# print(min(4,6))
# print(round(4.5))
# print(floor(4.5))
# print(ceil(4.5))
# print(sqrt(2))

#V6     INPUT FROM USER
# print(input("Enter your name: "))
# print(name)
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "!" + "(" + age + ")")

#V7     CALCULATOR
# num1 = input("Enter a Number: ")
# num2 = input("Enter a Number: ")
# result = float(num1) + float(num2)
# print(result)

# V8    MAD LIBS GAME
# color = input("Enter a color: ")
# noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are "+ color)
# print(noun + " are blue")
# print("I love "+ celebrity)

# V9      LISTS
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# print(friends[abs(int(input())%len(friends))])
# friends[1] = "Mike"
# print(friends)

# V10     LIST FUNCTIONS
# lucky_numbers = [4, 8, 5, 45, 456, 89]
# friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# APPEND DEMANDS A SINGLE ELEMENT
# EXTEND DEMANDS A SET-LIKE STRUCTURE
# friends.append("Creed")
# print(friends)
# friends.extend("Creed")
# print(friends)
# friends.extend(lucky_numbers)
# print(friends)
# friends.append(lucky_numbers)
# print(friends)
# friends.insert(1,"Kelly")
# friends.remove("Jim")
# friends.clear()
# friends.pop()
# print(friends.index("Kevin"))
# friends.append("Jim")
# print(friends.count("Jim"))
# friends2 = friends.copy()
# print(friends.reverse())
# print(friends)

# V11     TUPLES
# coordinates = (10,20)
# # coordinates[0] = 20
# print(coordinates)

# V12     FUNCTIONS
# def sayhi(name):
#     print("Hello " + str(name))
# sayhi(123)

# V13     RETURN STATEMENT
# def cube(num):
#     list = []
#     list.append(num*num*num)
#     return list
# print(cube(4))

# V14     IF STATEMENTS
# is_male = False
# is_tall = False
# if is_male and is_tall:
#     print("You are a Tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are a tall female")
# else:
#     print("You are a short female")

# V15     COMPARISIONS
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >=num3:
#         return num1
#     elif num2 >=num3:
#         return num2
#     else:
#         return num3
# print(max_num(32,32,33))

# V16     CALCULATOR
# num1 = float(input("Enter first number: "))
# op = input("Enter Operator: ")
# num2 = float(input("Enter second number: "))
# if op=="+":
#     num1 = num1 + num2
# elif op=="-":
#     num1 = num1 - num2
# elif op=="*":
#     num1 = num1 * num2
# elif op=="/":
#     num1 = num1 / num2
# else:
#     num1 = "Wrong Operator"
# print(num1)

# V17       DICTIONARIES
# monthConversions = {
#     "Jan":"January",
#     "Feb":"Feburary",
#     "Mar":"March",
#     "Apr":"April",
#     "May":"May",
#     "Jun":"June",
#     "Jul":"July",
#     "Aug":"August",
#     "Sep":"September",
#     "Oct":"October",
#     "Nov":"November",
#     "Dec":"Decemeber"
# }
# print(monthConversions.get("Jan","None"))
# print(monthConversions["Feb"])

# V18     WHILE LOOP
# i = 1
# while i<=10:
#     print(i)
#     i += 1
# print("Done with loop")

# V19     GUESSING GAME
# secret_word = "giraffe"
# tries = 3
# guess = ""
# while tries > 0:
#     guess=input("Enter The Secret Word: ")
#     if secret_word == guess:
#         break
#     else:
#         tries -= 1
# if tries == 0 :
#     print("GoodBye")
# else :
#     print("Welcome")

# V20     FOR LOOP
# for letter in "Giraffe Academy":
#     print(letter)
# friends = ["Jim", "Karen", "Kevin"]
# for friend in friends:
#     print(friend)
# for i in range(10):
#     print(i)
# for i in range(3,10):
#     print(i)
# for index in range(len(friends)):
#     print(friends[index])

# V21     EXPONENT FUNCTION
# print(2**3)
# def exp(num, pow):
#     res=1
#     for i in range(pow):
#         res*=num
#     return res
# print(exp(3,2))

# V22     2D LISTS AND NESTED LOOPS
# num_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for row in num_grid:
#     for col in row:
#         print(col)

# V23     TRANSLATOR
# phrase = "Hello I am you"
# def translate(phrase):
#     translated = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translated += 'g'
#         else:
#             translated += letter
#     return translated
# print(translate(phrase))

# V24     COMMENTS
# #SingleLine
# ''' 
# MultiLine
# '''

# V25     TRY EXCEPT
# try:
#     number = int(input('Enter a number: '))
#     print(number)
# except ValueError as err:
#     print("Yo Fool! " + str(err))

# V26     READ FILE
# people = open("./file.dat","r")
# for person in people.readlines():
#     print(person)
# people.close()

# V27      WRITE FILE
# people = open("./index.html","w")
# people.write("<div>Hello </div>")
# people.close()

# V28     MODULE AND PIPS
# # Python's package manager => pip
# import Tools
# print(Tools.funny(2))

# V28     CLASSES AND OBJECTS
# from Student import Student
# student1 = Student("Jim", "Business", 3.1, False)
# student2 = Student("Pam", "Art", 2.5, True)
# print(student2.name)

# V29 MULTIPLE CHOICE QUIZ
# class Question:
#     def __init__(self, question,correct):
#         self.question = question
#         self.correct = correct
# questions = [
#     Question("What color are apples?\n(a) Red\n(b)Green\n(c)Blue\n","a"),
#     Question("What color are bananas?\n(a) Red\n(b)Yellow\n(c)Orange\n","b"),
#     Question("What color are strawberries?\n(a)Magenta\n(b)Pink\n(c)Red\n","c")
# ]
# def run_test():
#     score=0
#     for q in questions:
#         if input(q.question)==q.correct:
#             score += 1
#     print("You scored " + str(score) + " out of " + str(len(questions)) + " correct")
# run_test()

# V30 CLASS FUNCTIONS
# from Student import Student2
# s1 = Student2("Oscar","Accounting", 3.1)
# s2 = Student2("Phyllis","Business", 3.8)
# print(s1.on_honor_role())
# print(s2.on_honor_role())

# V31 INHERITANCE
from ChineseChef import ChineseChef
chef = ChineseChef()
chef.make_chicken()
chef.make_fried_rice()