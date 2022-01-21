import random

print('H A N G M A N')
possible_answer = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(possible_answer)
dict_letters = {}
for i in range(len(answer)):
    dict_letters[i] = answer[i]
hidden_answer = list("-" *(len(answer)))
x = 0
guesses = set()
def make_a_move():
    global x, hidden_answer, guesses
    if x < 8:
        print()
        print(''.join(hidden_answer))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
            make_a_move()
        elif letter.islower() == False or letter.isalpha() == False:
            print('Please enter a lowercase English letter')
            make_a_move()

        if letter in answer and letter not in guesses:
            for k, v in dict_letters.items():
                if v == letter:
                    hidden_answer[k] = letter
            if '-' not in hidden_answer:
                print('You guessed the word!')
                print('You survived!')
                exit()
            else:
                guesses.add(letter)
                make_a_move()
        elif letter in hidden_answer or letter in guesses:
            print('You\'ve already guessed this letter')
            make_a_move()
        else:
            x += 1
            guesses.add(letter)
            print('That letter doesn\'t appear in the word')
            make_a_move()
    else:
        print('You lost!')
        exit()

def menu():
    print()
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        make_a_move()
    elif choice == 'exit':
        exit()
    else:
        menu()
menu()
