#exercise 8.5 of FUNCTION.
def describe_city(city_name, country = 'Nepal'):
    """display information about cities and country"""
    print(city_name.title() + " is in " + country + ".")

def main():
    describe_city(city_name = 'gorkha')
    describe_city(city_name= 'kolkota', country = 'India')
    describe_city(city_name= 'N.J', country= 'America')
    describe_city(city_name= 'Tokyo', country = 'Japan')
    

if __name__ == "__main__":
    main()