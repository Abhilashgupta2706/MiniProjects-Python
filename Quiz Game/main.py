print('''Hi there,
This a small Quiz game made by Abhilash Gupta.''')

# ------------------------Lists ------------------------

questions = ['In which year python was released? ',
             '"console.log()" is used in which language? ',
             'Which language does computer understand? ',
             'What does GPU stands for? ',
             'What is the full form of CSV? ',
             'Tuple is a mutable. (T/F) ',
             'Write a mathematical operator which returns the remainder.']
answers = ['1991',
           'javascript',
           'binary',
           'graphics processing unit',
           'comma separated value'
           'f',
           '%']

# ------------------------ Dictionary ------------------------

ques_with_ans = {
    'In which year python was released? ': '1991',
    '"console.log()" is used in which language? ': 'javascript',
    'Which language does computer understand? ': 'binary',
    'What does GPU stands for? ': 'graphics processing unit',
    'What is the full form of CSV? ': 'comma separated value',
    'Tuple is a mutable. (T/F) ': 'f',
    'Write a mathematical operator which returns the remainder.': '%'
}


# ------------------------ Functions ------------------------

def quizGameUsingLists(que_list, ans_list):
    score = 0
    submitted_ans = []

    for i in range(len(que_list)):
        print(que_list[i])
        ans_input = input('> ')

        submitted_ans.append(ans_input)

        if ans_input == ans_list[i]:
            score += 1

    percentage = round(score / len(que_list) * 100, 2)
    print(f'You gave total {score} correct answers, therefore your total percentage is {percentage}%')
    print(f'List of your submitted answers are {submitted_ans}')


def quizGameUsingDictionary(ques_dict):
    score = 0
    submitted_ans = []

    for keys in ques_dict:
        print(keys)
        ans_input = input('> ')

        submitted_ans.append(ans_input)

        if ans_input == ques_dict[keys]:
            score += 1

    percentage = round(score / len(ques_dict) * 100, 2)
    print(f'You gave total {score} correct answers, therefore you scored: {percentage}%')
    print(f'List of your submitted answers are {submitted_ans}')


def playingOrNot():
    playing = input('\nAre you willing to play this game? (y/n) ').lower()

    if playing == 'y':
        # quizGameUsingLists(questions, answers)
        quizGameUsingDictionary(ques_with_ans)
    elif playing == 'n':
        print('Then why you came here go away 😂👋🏻')
    else:
        print('Invalid input, Try again!')
        playingOrNot()


# Calling function to start the game
playingOrNot()
