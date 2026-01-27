# Part 2: Creating Your First Functions
'''
def say_hello():
    """Function with no parameters."""
    return "Hello, World!"
print(say_hello())

def greet(name):
    # function with one parameter
    return f"Hello, {name}!"
message = greet("Cassiddy")
print(message)

def multiply(num1, num2):
    # multiple parameters
    return num1 * num2
result = (multiply(4, 5))
print(result)
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}."
print(describe_person("Cassiddy", 19, "Honolulu"))

def introduce(name, job="Student", hobby="coding"):
    # default parameters
    """Introduce someone with default values for job and hobby."""
    return f"{name} is a {job} who enjoys {hobby}."
print(introduce("Cassiddy", "Developer", "Judo"))
'''

# Part 3: Return Values and Function Output
'''
def canDrive(age):
    return age >= 16
print(f"Is Cassiddy old enough to drive? {canDrive(19)}")

def favorite_sports(name):
    sports = ["Judo", "Wrestling", "Competitive Cheerleading"]
    return sports
print(f"Cassiddy's favorite sports are: {favorite_sports('Cassiddy')}")

def isPassword(password):
    return password == "securepassword123"
print(f"Is the password correct? {isPassword('securepassword124')}")
'''

# Part 4: Function Scope and Variables

'''
counter = 0
def increment_counter():
    global counter
    counter += 1
    return counter
print(f"Counter: {increment_counter()}") 
print(f"Counter: {increment_counter()}")


def local():
    x = 10  
    return x
print(f"Local variable x: {local()}")
'''

#Part 5: Practical Function Examples
'''
def countVowels(text):
    vowels="aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count
sample_text = "Hello, Cassiddy! Welcome to the world of Python."
vowel_count = countVowels(sample_text)
print(f'Number of vowels in the sample text: {vowel_count}')

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(f'5! (factorial): {calculate_factorial(5)}')

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(f'Is 29 a prime number? {is_prime(29)}')
'''

# Assessment Challenge

'''calculates the area of a rectangle given its length and width'''
def area_of_rectangle(length, width):
    return length * width
print(f'Area of rectangle (5, 10): {area_of_rectangle(5, 10)}')

'''checks if a number is even or odd'''
def isEven(number):
    '''Chek if number is divisible by 2 with no remainders'''
    return number % 2 == 0
'''Returns True if even, False if odd'''
print(f'Is 27 even? {isEven(27)}')

'''returns the largest number from a list of numbers'''
def returnLargest(list_of_numbers):
    '''max() pre-built function which returns the largest number in a list'''
    return max(list_of_numbers)
print(f'Largest number in [3, 5, 7, 2, 8]: {returnLargest([3, 5, 7, 2, 8])}')  

'''Welcomes a person with their name, city, and age'''
def introduce(name, city="Unknown", age="Unknown"):
    '''using default parameters for city and age ^'''
    return f"Hello, welcome {name}! I'm so glad you're {age} years old and live in {city}."
print(introduce("Cassiddy", age=19, city="Honolulu"))
