def main():
    pass
    
if __name__ == "__main__":
    main()

def show_magicians (names):
    for i in names:
        print(i.title())

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ": the Great."
        great_magicians.append(great_magician)

    for i in great_magicians:
        magicians.append(i)

def main():
    magicians = ['abhi', 'abhijeet', 'anu', "ram"]
    make_great(magicians)
    show_magicians(magicians)
    
if __name__ == "__main__":
    main()
