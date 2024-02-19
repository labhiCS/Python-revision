#Chapter 7 userinput and while loops!!
prompt = ("\nEnter any number: ")
prompt += ("\nEnter 'quit' to end the program. ")

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#Practicing using while loop!!
current_number = 9
while current_number <= 18:
    print(current_number)
    current_number += 2

