class Users:
    course = 'python'
    
    @classmethod
    def greet():
        print('hello world')

user1 = Users()

print(user1.course)

Users.greet()

