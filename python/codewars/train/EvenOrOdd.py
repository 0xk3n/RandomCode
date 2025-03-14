"""
Create a function that takes an integer as an argument and returns
"Even" for even numbers or "Odd" for odd numbers.
"""

def even_or_odd(number):
    '''if int(number) % 2 == 0:
        print(f"{number} is Odd")
    elif int(number) != 0:
        print(f"{number} is Even")
    else: 
        pass '''
    return "Even" if number % 2 == 0 else "Odd"
#list = [2, 1, 2, -1, -2, 0]
#for i in list:
even_or_odd(2)
