'''Hangman-game'''
import time
import numpy as np


def init():
    '''Hangman initialisation'''
    max_mistakes = 5
    print("Hi, user! What's your name?")
    usr_nm = input()
    print("Dear {}, welcome to the game Hangman!".format(usr_nm))
    with open('words_list.txt', 'r') as file_obj:
        words_list = list(file_obj.read().split())
    hangman(words_list, max_mistakes)


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


def get_wish():
    '''Ask the player does he would like to play again ?'''
    print("Would you like to play again? y or n", "\n")
    again = input().lower()
    while again not in ('n', 'y'):
        print("I didn't get that.")
        print("Would you like to play again? y or n", "\n")
        again = input().lower()
    return again


def pick_a_new_word(words_list, max_mistakes):
    '''Choose new word from words_list
    Told to the user about the rules'''
    print("Let's pick a new word...")
    time.sleep(1)
    word = np.random.choice(words_list)
    print("The hidden word contains {} letters!".format(len(word)))
    print("You might make {} mistakes in total.".format(max_mistakes))
    print("You can guess one letter per round.", "\n")
    return word


def hangman(words_list, max_mistakes):
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
    word = pick_a_new_word(words_list, max_mistakes)
    guessed, wrong, cur_mistakes = [], [], 0
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
            wish = get_wish()
            cur_mistakes = max_mistakes
            if wish == 'n':
                print('Goodbye! Thank you for playing.')
            elif wish == 'y':
                hangman(words_list, max_mistakes)
