'''Module tests'''
from hangman import check_letter, print_word, pick_a_new_word


def test_check_letter():
    '''Module test by correct work function check_letter'''
    assert check_letter('t',
                        'test',
                        1,
                        ['e'],
                        ['o']) == (1, ['e', 't'], ['o'])
    assert check_letter('e',
                        'check',
                        1,
                        ['e'],
                        ['o']) == (1, ['e'], ['o'])
    assert check_letter('a',
                        'letter',
                        1,
                        ['e'],
                        ['o']) == (2, ['e'], ['o', 'a'])


def test_print_word():
    '''Module test by correct work function print_word'''
    assert print_word('test', ['t']) == 't**t'
    assert print_word('print', ['i', 'p']) == 'p*i**'
    assert print_word('word', ['a']) == '****'


def test_new_word():
    '''Module test by correct work function pick_a_new_word'''
    assert pick_a_new_word(['pepa'], 5) == ('pepa')
    assert pick_a_new_word(['pepe', 'pepe'], 5) == ('pepe')
