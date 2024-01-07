def user_name(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
person_names = ['anup', 'anusha', 'abhi']
user_name(person_names)