# Handy library of mathematical functions
# Name: Cassiddy Ginoza
# Date: Jan. 27, 2026

def midpoint(num1, num2):
    ''' Calculate the midpoint between two numbers'''
    mid = (num1 + num2) / 2
    return mid

def sqrt(number):
    ''' Calculate the square root of a number'''
    if number < 0:
        return None
    return number ** 0.5

def exponent(base, exp, precision=2):
    '''Calculate the exponentiation of a base to a given exponent'''
    result = base ** exp
    rounded_result = round(result, precision)
    return rounded_result

def max(num1, num2):
    '''Return the maximum of two numbers'''
    return num1 if num1 >= num2 else num2

def min(num1, num2):
    '''Return the minimum of two numbers'''
    return num1 if num1 <= num2 else num2


def apply_function(num1, num2, func):
    result = func(num1, num2)
    return f"The function {func.__name__} {num1},{num2} = {result}"