people = ['Zahid','Hasan','Papon','Takle']

# simple for loop

for person in people:
    print (f'Current person:{person}')

# Break
for person in people:
    if person == 'Papon':
     break
    print (f'Current person:{person}')

# Continue
for person in people:
    if person == 'Papon':
     continue
    print (f'Current person:{person}')

# range 
for i in range(len(people)):
    print(people[i])

for i in range(0,11):
    print(f'Number: {i}')


# While loops

count = 0
while count <= 10:
    print(f'count:{count}')
    count +=1