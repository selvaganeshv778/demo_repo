class Users:
    course = 'python'

    #Similar to constructor in python
    def __init__(self, name) :
        self.name = name
        print('new user created')
        self._mobile = 7871457880

    #class method without decorator
    def greet():
        print('hello world')

    #instance method
    def greeting_from_instance(self):
        print("greeting from instance")

    def get_mobile(self):
        return self._mobile

    #by creating this method we can get the private attribute as attribute
    @property
    def mobile(self):
        return self._mobile

class Students:

    def __init__(self,name,age,role_number):
        self.name = name
        self.age = age
        self._role_number = role_number

    def  get_role_number(self):
        return self._role_number
    def  set_role_number(self,number):
        self._role_number = number
    role_number = property(get_role_number, set_role_number)

user1 = Users('selva')

print(user1.course)

Users.greet()

print('calling from instance')
user1.greeting_from_instance()

print(user1.get_mobile())
print('printing as attribute itself after using @property annotation')
print(user1.mobile)

s1 = Students('anand',25,2216)

print(s1.role_number)