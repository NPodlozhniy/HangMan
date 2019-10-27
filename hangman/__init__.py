'''Hangman-game'''
import numpy as np


def init():
    '''Hangman initialisation'''
    guessed, wrong = [], []
    max_mistakes = 5
    print("Hi, user! What's your name?")
    usr_nm = input()
    print("Dear {}, welcome to the game Hangman!".format(usr_nm))
    with open('words_list.txt', 'r') as file_obj:
        words_list = list(file_obj.read().split())
    hangman(words_list, guessed, wrong, max_mistakes)


def check_letter(guess, word, cur_mistakes, guessed, wrong):
    '''Check that hidden word contin input letter'''
    if guess in guessed or guess in wrong:
        print("Letter already guessed", "\n")
    elif guess in word:
        print("Hit!", "\n")
        guessed.append(guess)
    else:
        cur_mistakes += 1
        print("Missed, mistake {} out of {}".format(cur_mistakes,
                                                    5),
              "\n")
        wrong.append(guess)
    return cur_mistakes, guessed, wrong


def print_word(word, guessed):
    '''Print word on a screen'''
    out = ''
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "*"
    print("The word: {}".format(out),
          "\n")
    return out


def play_again(word, words_list, cur_mistakes, guessed, wrong):
    '''Input: word, words_list, cur_mistakes, guessed, wrong
    Asks the player to play again
    Returns new words,
    cur_mistakes to 0,
    guessed and wrong to []
    if 'y' is pressed.
    Change cur_mistakes to max_mistakes if 'n' is pressed'''
    clear_answer = False
    while clear_answer is False:
        again = print("Would you like to play again? y or n",
                      "\n")
        again = input().lower()
        if again == 'n':
            clear_answer = True
            print('Goodbye! Thank you for playing.')
            cur_mistakes = 5
        elif again == 'y':
            print("Let's pick a new word...")
            word = np.random.choice(words_list)
            print("The hidden word contains {} letters!".format(len(word)))
            guessed = []
            wrong = []
            cur_mistakes = 0
            clear_answer = True
        else:
            print("I didn't get that.")
    return word, cur_mistakes, guessed, wrong


def hangman(words_list, guessed, wrong, max_mistakes):
    '''Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the hidden word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the hidden word.
    * After each round, you should also display to the user the
      partially guessed word so far.
    * After each win or loss, user have a chance to choose
      between two variants: left the game and continue'''
    word = np.random.choice(words_list)
    print("The hidden word contains {} letters.".format(len(word)))
    print("You might make {} mistakes in total.".format(max_mistakes))
    print("You can guess one letter per round.", "\n")
    cur_mistakes = 0
    while max_mistakes > cur_mistakes:
        print("Guess a letter:")
        cur_mistakes, guessed, wrong = check_letter(input(),
                                                    word,
                                                    cur_mistakes,
                                                    guessed,
                                                    wrong)
        out = print_word(word, guessed)
        if out == word or max_mistakes == cur_mistakes:
            if out == word:
                print("You won!")
            else:
                print("You lost!", "\n")
                print("Correct word: {}".format(word))
            word, cur_mistakes, guessed, wrong = play_again(word,
                                                            words_list,
                                                            cur_mistakes,
                                                            guessed,
                                                            wrong)
