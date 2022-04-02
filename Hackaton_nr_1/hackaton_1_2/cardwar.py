import random
# Cars from 2 to 10 and next to W,Q,K,A in program counterpart 0 up to 11
# S - spade
# C - club
# H - heart
# D - diamond
#
def decription_card(dict_element):
    return (str(descript_value_card(dict_element['number'])+str(descript_color_card(dict_element['color']))))

def descript_value_card(value):
    if (value)<8:
        return (f"{value+2}")
    elif(value)==8:
        return ("Jack")
    elif (value)==9:
        return("Queen")
    elif (value) == 10:
        return("King")
    elif (value) == 11:
        return ("As")

def descript_color_card(value):
    if value =='S':
        return ' Spade'
    elif value =='C':
        return ' Club'
    elif value =='H':
        return ' Heart'
    else:
        return ' Diamond'



color_range = ['S','C','H','D']
deck={}

# Preapre deck = []
card_index=0
for number in range (0,12):
    for color in color_range:
        deck[card_index]={'number':number,'color':color}
        card_index+=1

# Start game
choose_card= (random.sample(sorted(deck),20))

first_user_card = choose_card[0::2]
second_user_card = choose_card[1::2]

new_first_user_card=[]
new_second_user_card=[]

for card in range (0,len(first_user_card)):
    if deck[first_user_card[card]]['number']<deck[second_user_card[card]]['number']:
        print (f" Przegrałes. Twoja karta {decription_card(deck[first_user_card[card]])} jest słabsza od karty przeciwnika{decription_card(deck[second_user_card[card]])}")
        new_second_user_card.append(second_user_card[card])
        new_second_user_card.append(first_user_card[card])
    elif deck[first_user_card[card]]['number']==deck[second_user_card[card]]['number']:
        print(f" Remis. Wasze karty {decription_card(deck[first_user_card[card]])} i {decription_card(deck[second_user_card[card]])} są równe")
    else:
        print(f" Wygrałeś. Twoja karta {decription_card(deck[first_user_card[card]])} jest silniejsza od karty przeciwnika {decription_card(deck[second_user_card[card]])}")
        new_first_user_card.append(second_user_card[card])
        new_first_user_card.append(first_user_card[card])
# give cards

