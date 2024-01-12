def main():
    pass
    
if __name__ == "__main__":
    main()  


person_name = {
    'first_name': 'Abhishek', 
    'last_name': 'Lamichhane',
    'age': '19',
    'city': 'kathmandu',
    }

print(person_name["first_name"] + person_name["last_name"])
print(person_name["age"] + "yrs old")
print("Lives in " + person_name["city"].title() + " city")
print("\n")

for i, j in person_name.items():
    print(i + " is " + str(j))