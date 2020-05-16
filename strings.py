name = 'Zahid'
age = 23

# concatenate

#print ('Helllo, my name is ' + name + 'and i am '+ str(age))

# string formatting 

#arguments by position

#print ("My name is {name} and i am {age}".format(name = name, age = age))

# F-Strings 

#print (f'Hello, my name is {name} and i am {age}')

s = 'hello~World'

# Capitalize String 
print(s.capitalize())

# Make all uppercase 
print (s.upper())

# make all lower 
print (s.lower())

# swap case 
print (s.swapcase())  

# get length 
print(len(s))

# replace
print (s.replace('World', 'everyone'))

#count 
sub ='h'
print (s.count(sub))

# starts with 
print (s.startswith ('hello'))

# ends with 
print (s.endswith ('d'))

# Split into a list 
print (s.split())

# find position
print (s.find('o'))

# is all alphanumeric 
print (s.isalnum())

#is all alphabetic 
print (s.isalpha())

# is all numeic 
print (s.isnumeric())