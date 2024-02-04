#exercise 9.1!!
class Resturant():
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print("My resturant name is " + self.resturant_name.title() + ".")
        print(self.cuisine_type.title() + " is available.")
    
    def open_resturant(self):
        print(self.resturant_name.title()+ " is opened.")

rest_1 = Resturant('Gorkhali Vansaghar', 'Neplese dish')
rest_2 = Resturant('chineese cousine', 'chineese')

rest_1.describe_resturant()
rest_1.open_resturant()
print("\n")
rest_2.describe_resturant()
rest_2.open_resturant()