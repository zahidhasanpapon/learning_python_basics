# Create a dict 

person = {
    'first_name':'Zahid',
    'last_name':'Hasan',
    'age': 23
}


# use a constructor

# person2 = dict(first_name='Murchhana', last_name='Hasan')

# get value 
print(person['first_name'])
print(person.get('last_name'))

#  add key/value

person['phone'] = '01917507560'

#get dict keys
print(person.keys())

#get dict items
print(person.items())

# copy a dict 

person2 = person.copy()
person2['city'] = 'Dhaka'

# Remove item 
del(person['age'])
person.pop('phone')

# clear
person.clear()

# get length
print (len(person2))

print(person2)


# list of dict 

people = [
    {'name':'Martha', 'age':30},
    {'name':'Kevin','age':25}
]

print(people[1]['name'])



#print (person2,type(person2))