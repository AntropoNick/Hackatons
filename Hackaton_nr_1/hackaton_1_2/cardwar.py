import random
# Cars for 2 to 10 and nest to W,Q,K,A in program counterpart 0 tp 11
# S - spade
# C - club
# H - heart
# D - diamond

def decription_card(dict_element):
    if (dict_element)<[8]:
        print (list(dict_element)-2,end=" ")
    elif(dict_element)==8:
        print ("Jack",end="")
    elif (dict_element)==9:
        print("Queen", end="")
    elif (dict_element) == 10:
        print("King", end="")
    elif (dict_element) == 11:
        print("As", end="")


color_range = ['S','C','H','D']
deck={}
# Preapre deck = []
card_index=0
for number in range (0,12):
    for color in color_range:
        deck[card_index]={number:color}
        card_index+=1
chose_card= (random.sample(sorted(deck),20))

first_user_card = chose_card[0::2]
second_user_card = chose_card[1::2]



print(first_user_card)
for card in first_user_card:

    print (int(deck[card].keys()))
    #decription_card(deck[card].keys())
# give cards

