import json 

# sample JSON

userJSON ='{"first_name": "Zahid", "last_name":"Hasan", "age": 23}'

# parse to dict

user = json.loads(userJSON)



print(user)
print (user['first_name'])

car = {'make': 'Ford', 'model':'Mustang','year':1970}

carJSON = json.dumps(car)

print(carJSON)
