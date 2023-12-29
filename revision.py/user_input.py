#Chapter 7 userinput and while loops!!
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit/q':
    message = input(prompt)

    if message != 'quit/q':
        print(message)

#Practicing using while loop!!

current_number = 0
while current_number <= 15:
    print(current_number)
    current_number += 1
