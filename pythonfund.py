# Tasks:
# Function: add_numbers
#A function named add_numbers that takes two parameters num1 and num2, and returns the sum of the two numbers.

def add_numbers(num1, num2 ):
    return num1 + num2

total=add_numbers(num1=3,num2=2)
print(total)

# Function: is_even (2 points)
# function named is_even that takes a single parameter number and returns True if the number is even, and False otherwise.

def is_even(number):
    if number % 2 ==0:
        print(True)
    elif number % 2 !=0:
         print(False)

is_even(3)

# Function: reverse_string
# function named reverse_string that takes a string text as input and returns the reversed version of that string.
def reverse_string():
    #using the slicing string[::-1]
    string=(input("What is your name?")).upper()
    return string[::-1]

result=reverse_string()
print(result)

# # Function: count_vowels (2 points)
# # Python function named count_vowels that takes a string text as input and returns the count of vowels (a, e, i, o, u) in the string. Ignore case sensitivity.
# def count_vowels():
#     name= str(input("Where are you from? "))
#     count =0
#     # using the for loop
#     for vowel in name:
#         if vowel in count:
#             count[vowel] +=1
#     return count
#     if name.upper() in ("a","e","i","o","u"):
#         return name

# results = count_vowels()

# print(results)

    
# # Function: calculate_factorial (2 points)
# # Write a Python function named calculate_factorial that takes a non-negative integer n as input and returns the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.


def calculate_factorial(n):
    n=int(input("Choose any number"))
    if n ==0:
        return 1
    else:
        return n *(n<=1)

calculate_factorial(4)


# # Function: apply_decorator (1 point)
# # Write a Python function named apply_decorator that takes a function func as input and applies a decorator named decorator_func. The decorator should simply print "Decorator Applied" before calling the original function.

# # Sequences: Sort List of Tuples (1 point)
# # Given a list of tuples where each tuple contains a name and an age, write a Python function named sort_by_age that sorts the list of tuples by age in ascending order.

# # Sets and Dictionaries: Merge Dictionaries (1 point)

# # Write a Python function named merge_dicts that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values should be summed up.
# # Object-Oriented Programming: Class Creation (2 points)

students= {
  "MoringaStudents": ["Sherlyne", "Mary", "John", "Hilda"],
  "Total": 3 }
cities= {
    "Kenya Cities": ["Nairobi", "Mombasa", "Nakuru", "Mombasa"]}
def merg_dicts(students,cities):
  #the different dictionaries of students and cities in kenya 
  for key in cities.keys():
    if key in students:
      students[key].extend(cities[key])
    else:
      students[key]=cities[key]
  return students
  
studentsCities= merg_dicts(students,cities)
print(studentsCities)
  
# , # A python class named Car with the attributes: make, model, year. 
# # the function Implements a method named display_info that prints out the car's information. 

class Car: 
    def __init__(self,make,model,year):
        self.make =make 
        self.model=model
        self.year =year
 # a method named display_info 

    def display_info(self):
       print(f"Car's information:{self.make},{self.model}, {self.year}")

# #The instance = Toyota 
# Toyota=Car("Toyota","Camri",2024)
# print(Toyota.display_info())
