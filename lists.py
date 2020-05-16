# create a list 

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# use a constructor 
# numbers2 = list((1,2,3,4,5))

# get a value 
print (fruits[1])

# get length 
print (len(fruits))

# Append 
fruits.append ('Mangoes')

# remove from list 
fruits.remove('Grapes')

# isnert into position

fruits.insert(2, "Strawberries")

# remoove with pop

fruits.pop (2)

# Reverse the list 
fruits.reverse()

# Sort List 
fruits.sort()

# Reverse Sort 
fruits.sort(reverse=True)

# Change value 
fruits[0] = "Blueberries"

print(fruits)