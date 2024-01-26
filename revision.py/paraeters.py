def user_name(first_name,last_name,  age=0):
    print(first_name.title() + " " + last_name + " is " + age + "years old.")

def main():
    user_name(first_name = 'abhi', age= '26', last_name='lamichhane')
    user_name(first_name="nani", last_name= "simkhada", age = '80')
    user_name(first_name="anup", last_name= "Thapa")

if __name__ == "__main__":
    main()