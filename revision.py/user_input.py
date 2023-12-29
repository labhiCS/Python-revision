#Chapter 7 userinput and while loops!!
user_input = input("Enter any number: ")
user_input = int(user_input)

if user_input>= 20:
    print("You are old enough to drink alcohol.")
else:
    print("You are too small for it ")

print("\n")

#Practicing using while loop!!

current_number = 4
while current_number <= 18:
    print(current_number)
    current_number += 2

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)