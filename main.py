from do_quiz import quiz
from data import clr
from time import sleep

in_game = True
user_name = input('Hello, welcome to quiz program, please enter your name\n> ').strip().capitalize()
clr()
print(f'Hi {user_name}!')
sleep(1)
clr()

while in_game:
    user_choice = input(f'{user_name} enter /new_quiz to start new quiz\nEnter /exit to exit the app\n> ').strip()
    if user_choice == '/exit':
        in_game = False
        clr()
        print(f'Bye {user_name}!')
        sleep(1)
        clr()
    elif user_choice == '/new_quiz':
        quiz(user_name)
        clr()
    else:
        clr()
        print(f'I dont understand you {user_name}:(')
        sleep(2)
        clr()
