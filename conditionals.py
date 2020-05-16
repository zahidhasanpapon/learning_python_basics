x = 20
y = 20

# simple if
if x > y:
    print(f'{x} is grrater than {y}')

# if/else
if x > y:
    print(f'{x} is grrater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif 
if x > y:
    print(f'{x} is grrater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if 
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')

# logical operator 
if x > 2 and x<=10:
        print(f'{x} is greater than 2 and less than or equal to 10')
#or
if x > 2 or x<=10:
        print(f'{x} is greater than 2 or less than or equal to 10')


# not 
if not(x==y):
    print(f'{x} is not eqaul to {y}')

# membership operators 

numbers = [1,2,3,4,5]

# In
if x in numbers:
    print(x in numbers)

# Not in 
if y not in numbers:
    print(y in numbers)


# Identity Operators 

#is
if x is y:
    print(x is y)

# is not 
if x is not y:
    print(x is not y)




