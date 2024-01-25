def user_name(person_name,last_name,  age=0):
    print(person_name.title() + " " + last_name + " is " + age + "years old.")

def main():
    user_name(person_name = 'abhi', age= '26', last_name='lamichhane')
    user_name(person_name="nani", last_name= "simkhada", age = '80')

if __name__ == "__main__":
    main()