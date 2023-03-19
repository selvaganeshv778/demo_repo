class Users:
    course = 'python'

    #class method without decorator
    def greet():
        print('hello world')

    #instance method
    def greeting_from_instance(self):
        print("greeting from instance")

user1 = Users()

print(user1.course)

Users.greet()

print('calling from instance')
user1.greeting_from_instance()


class Students:
    pass
