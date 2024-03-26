class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age 
        self.profession = profession.title()
    
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is a " + self.profession)

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name + ".")

user = User('abhi', 'guragain', 16, 'student.')
user_1 = User('anu', 'thapa', 25, 'doctor. ')
user_2 = User('rose', 'lamichhane', 19, 'Nures' )

user.describe_user()
user.greet_user()
print("\n")


user_1.describe_user()
user_1.greet_user()
print("\n")

user_2.describe_user()