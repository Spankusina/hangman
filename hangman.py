from random import *
from os import system

def get_word():
    w = choice(word_list)
    return w.upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word, lvl):
    system('cls')
    print('Давайте играть в угадайку слов!')
    tr = 6
    guessed = False
    guessed_letters = []
    guessed_words = []
    if lvl == '1':
        word_completion = word[0] + '*' + word[-1]
    elif lvl == '2' or lvl == '3':
        word_completion = word[0] + '*'*(len(word)-1)
    else:
        word_completion = '*'*len(word)
    while not guessed:
        if tr > 0:
            print(display_hangman(tr))
        else:
            print(display_hangman(tr))
            print('Вы проиграли :(')
            print('Загаданное слово было:', word)
            guessed = True
            break
        print(word_completion)
        char = input('Введите букву или слово целиком: ').upper()
        if not char.isalpha():
            system('cls')
            print('Это не буква, попробуйте еще')
            continue
        if len(char) > 1:
            if char in guessed_words:
                system('cls')
                print('Такое слово уже называли, попробуйте еще')
                continue
            else:
                if char == word:
                    print('УРА! ПОБЕДА!')
                    guessed = True
                else:
                    guessed_words.append(char)
                    tr -= 1
                    system('cls')
                    print('К сожалению, неверное слово, попробуйте еще')
        elif len(char) == 1:
            if char in guessed_letters:
                system('cls')
                print('Такую букву уже называли, попробуйте еще')
                continue
            else:
                if char in word:
                    system('cls')
                    
                    guessed_letters.append(char)
                    for index, s in enumerate(word):
                        if char == s:
                            word_completion = word_completion[:index] + char + word_completion[index+1:]
                    if word_completion == word:
                        print('УРА! ПОБЕДА! Вы открыли все буквы!')
                        print('Было загадано слово', word)
                        guessed = True
                    else:
                        print('Есть такая буква!')
                else:
                    guessed_letters.append(char)
                    tr -= 1
                    system('cls')
                    print('К сожалению, такой буквы нет, попробуйте еще')   
                

with open('hangman.txt', 'rt', encoding='utf-8') as r:
    words = r.read()

word_list = words.split()

level = (input('''Выберите уровень:\n1) Самый легкий (2 подсказки, длина слова 3 буквы)\n2) Немного посложнее (1 подсказка, длина слова до 4 букв\n3) Средний (1 подсказка, длина слова до 5 букв\n4) Без ограничений (нет подсказок, длина слова любая\n\n'''))

if level == '1':
    word_list = [i for i in word_list if len(i) <= 3]
elif level == '2':
    word_list = [i for i in word_list if len(i) <= 4]
elif level == '3':
    word_list = [i for i in word_list if len(i) <= 5]

game = 'д'

while game == 'д':
    word = get_word()
    play(word, level)
    game = input('Сыграем еще? (д/н) ')
