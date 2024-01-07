def main():
    pass
    
if __name__ == "__main__":
    main()

def user_name(names):
    for i in names:
        msg = "Hello, " + i.title() + "!"
        print(msg)
        
person_names = ['anup', 'anusha', 'abhi']
user_name(person_names)