from data import questions, clr
from random import sample
from time import sleep

def quiz(user_name):
    clr()
    corect_answewr = 0
    amount_of_questions = int(input('How many questions do you want to have?\nEnter a number between 3 and 10:').strip())
    clr()
    if 11>amount_of_questions>2:
        questions_for_quiz = sample(questions, amount_of_questions)

        for question_n_answer in questions_for_quiz:
            print(f'Question: {question_n_answer[0]}\n\n')
            user_answer = input('Enter your answer:').strip().capitalize()
            if user_answer == question_n_answer[1]:
                clr()
                print('Corect!')
                corect_answewr+=1
                sleep(2)
                clr()
            else:
                clr()
                print('Incorect!')
                sleep(2)
                clr()
        print(f'{user_name}, your score: {corect_answewr}/{amount_of_questions}')
        sleep(2)
        clr()
    else:
        quiz(user_name)
