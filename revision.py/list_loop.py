#Practicing loop in list!!
bikes = ["BMW", "ducati", "honda", "splinter"]
for i in bikes:
    print(i.title() + ", it's a great Bike!!")
    print("I love to ride a " + i.title() + ".\n")

# Using range().
for i in range(1, 8):
    print(i)

even_numbers = list(range(2, 21, 2))
print(even_numbers)

square_numb = []
for value in range(1, 15):
    square = value ** 2
    square_numb.append(square)

print(square_numb)
#upto page 72practiced