# Create a class

class User:
    # constructor 
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age

    def greeting (self):
        return f'My name is {self.name} and i am {self.age} '
    def has_birthday(self):
        self.age += 1


# extend class

class Customer (User):
      # constructor 
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self,balance):
        self.balance = balance 
    def greeting (self):
        return f'My name is {self.name} and i am {self.age} and my blanace is {self.balance}'



# init user object 
zahid = User('Zahid Hasan', 'zahid@email.com', 23)
# inti customer Object 

murchhana = Customer('Murchhana Hasan', 'murchhana@email.com', 22)
murchhana.set_balance(500)
print(murchhana.greeting())

zahid.has_birthday()
print(zahid.greeting())
