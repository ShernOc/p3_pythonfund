# Function add_numbers that adds two numbers 
def add_numbers(num1, num2 ):
    return num1 + num2

total=add_numbers(num1=3,num2=2)
print(total)

# Function: is_even that evaluates if the number is even or not. 

def is_even(number):
    if number % 2 ==0:
        print(True)
    elif number % 2 !=0:
         print(False)
is_even(3)

# function prompts the user to input a string which is then converted to string uppercase .upper(), and reversed using slice notation  [::-1] 

def reverse_string():
    #using the slicing string[::-1]
    string=(input("What is your name?")).upper()
    return string[::-1]
result=reverse_string()
print(result)

# functions finds the number of vowels in a string. 
def count_vowels(text):
    # string containing the vowels
    vowels= "aeiou"
    # converts string to lowercase 
    text=text.lower()
    # initialize counter to 0: as the number of vowels
    count =0
    # loops through each character (char) in the text and checks each character has a vowel listed in vowels
    for char in text:
        if char in vowels:
           # if a vowel is found it increases the count by 1.
           count +=1
    # return number count of vowels found in the text. 
    return count

print(count_vowels("sherlyne"))

#Function that takes a non-negative integer n as input and returns the factorial of that number.
def calculate_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        # shows the factorial calculation (n*(n-1))
        return n * calculate_factorial(n-1)
result=calculate_factorial(4)
print(result) 

#Decorator function that takes a function and returns a function. 
# apply_decorator takes a (function) as an argument
def apply_decorator(func):
    # decorator_fun calls the (func) and prints/ and acts as a wrapper
    def decorator_func():
        func()
        print("Decorator Applied")
    return decorator_func
def get_func(): 
        print("New function being called ")

 #applies and calls the decorator to get_func which gets the appy_decorator

get_func=apply_decorator(get_func)
# provides the output of new function and appy_decorator function. 
get_func()

#Tuples: created a list of tuples and sorted the list by age in ascending order. 
name_age_tuple = ([("sherlyne", 10), ("making", 24), ("John", 56),("Mary", 19)])
def sort_by_age(name_age_tuple):
    #used the sorted*() with  key: labda to sort the list based on the second element (age)of x[1]; [1] is the index (56 in john,56)
    return sorted(name_age_tuple,key=lambda x:x[1])

print(sort_by_age(name_age_tuple))
   
# Created two dictionaries 
students= {
  "MoringaStudents": ["Sherlyne", "Mary", "John", "Hilda"],
  "Total": 3 }
cities= {
    "Kenya Cities": ["Nairobi", "Mombasa", "Nakuru", "Mombasa"]}

# function merges the students and cities dictionaries 
def merg_dicts(students,cities):
  #for loop that iterates over the key in cities, and if the key exist in students it extends the list, if not a key value from cities is added to students.
  for key in cities.keys():
    if key in students:
      students[key].extend(cities[key])
    else:
      students[key]=cities[key]
      # returns a new student dictionary with cities  
  return students
  
studentsCities= merg_dicts(students,cities)
# returns the merged dictionaries. 
print(studentsCities)
  
# OOP: Class of Car  
class Car: 
    def __init__(self,make,model,year):
        self.make =make 
        self.model=model
        self.year =year
 # a method named display_info 

    def display_info(self):
       print(f"Car's information:{self.make},{self.model},{self.year}")

# The instance = Toyota 
toyota=Car("Toyota","Camri",2024)
toyota.display_info()
