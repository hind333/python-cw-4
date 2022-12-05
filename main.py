def my_name(name):
 print(f"my name is {name}")

my_name("hind")

def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")

my_meal("pizza","orange juice")

def cube(number):
    return number ** 3
cube(8)
def by_three(number):
    if number  % 3 == 0:
       return cube(number) 
    else: False