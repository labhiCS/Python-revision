def make_shirt(size, text_message):

    print("The size of the t-shirt is " + str(size))
    print("The message printed on a t-shirt is " + text_message.upper())

def main():

    make_shirt(30, 'ram')
    make_shirt(size = 30, text_message = 'ram')

if __name__ == "__main__":
    main()
    