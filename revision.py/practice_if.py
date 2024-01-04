fruits = ["apple", "banana", "mango", "popaya"]

for i in fruits:
    if i == "Banana":
        print(i.upper() + " = True")
    else:
        print(i.title()) 

# Using if loop
age = 27

if age < 28:
    price = 50
elif age <18:
    price = 70
elif age < 25:
    price = 100
else:
    price = 25
print("The price of alcohol is $" + str(price) + ".")