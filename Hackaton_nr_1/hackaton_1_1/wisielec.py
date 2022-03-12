# Hangman - the game
# The game is to guess a random  word chooseby the computer.
# The player is informed about the length of the searched word and numer of chance to guesse the word.
# The word to guess is printing as a row of underscores, wher each underscore represent each letter of the word.
# In the next steps player guesse the letters. If  a letter which occurs in the word,
# the program writes it in all its correct positions.
#
# The player guessing the word may, at any time, attempt to guess the whole word, typing char '?'
# If the word is correct, the game is over and the guesser wins. Otherwise, the game is going on.
# The player can also win by guessing all the letters that appear in the word.

import random

find_position=[]
words = ["python","noc","praca","lato","radio"]


def intro():
    width_sceen = 90
    print(width_sceen * "-")
    str = "GRA WISIELEC"
    print("|", (int((width_sceen - len(str))/2)-3) * " ", str, (int((width_sceen - len(str))/2)-3)*" ","|")
    print(width_sceen * "-")
    print ("""Witamy w grze. Twoim zadaniem jest  odgadniecie tajnego słowa wylosowanego przez komputer.
W kolejnych krokach będziesz odgadywać litery wchodzące w skład szukanego słowa. Jeżeli na
podstawie odkrytych liter jesteś w stanie odgadnąć słowo wciśnij klawisz '?' i wpisz słowo. 
Powodzenia!""")

def find_word(word,chance):
    char = input(f"Próba nr {chance+1}. Podaj litere lub '?' aby odgadnąć słowo: ")
    if char =='?':
        return (check_word(word))
    else:
        match="--> Pudło! "
        for index in range(0,len(word)):
            if char==word[index]:
                find_position[index]=1
                match = "--> Odgadłes literke! "
        show_find_chars(word,match)
        if sum(find_position)==len(word):
            print("Gratulacje. Odgadłeś wszystkie litery poszukiwanego słowa")
            return 1
        else:
            return 0

def show_find_chars(word,match):
    print (match,end="")
    print ("Twoje słowo aktualnie wygląda w ten sposób: ",end="")
    for index in range (0,len(word)):
        if find_position[index]:
            print (word[index],end="")
        else:
            print("_", end="")
    print()

def check_word(word):
    user_word = str(input("Podaj słowo: "))
    if word == user_word:
        print("Gratulacje! Wygrałeś. Tego słowa szukano.")
        return 1
    else:
        print("To nie to słowo")
        return 0

# Show intro text
intro()
# Choose one word from list
random_word=words[random.randrange(0,len(words))]
# Compute number of chances for user to find word
chances = 1*len(random_word)
find_position=[0]*len(random_word)

print(f"\nWylosowane dla Ciebie słowo składa się z {len(random_word)} liter:",len(random_word)*"_","\n")
print (f"Masz {chances} prób na odgadnięcie tajnego słowa. Powodzenia!")

for index_chance in range (0,chances):
    if find_word(random_word,index_chance):
        break
    if index_chance == chances - 1:
        print("Koniec prób. Spróbuj odgadnąć słowo.")
        check_word(random_word)





