# Card Draw
# Author: Sylvia Chapman Kent
# Draws two cards from a shuffled deck and prints the value and suit of each

import requests
import json
import itertools
#get shuffled deck
url1="https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response1=requests.get(url1)
deck=response1.json()
#record deck id
deck_id=deck["deck_id"]
#draw 2 cards from shuffled deck
url2=(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
response2=requests.get(url2)
draw=response2.json()
#record details of all cards [1]
first_card=draw['cards'][0]
second_card=draw['cards'][1]
third_card=draw['cards'][2]
fourth_card=draw['cards'][3]
fifth_card=draw['cards'][4]
#print value and suit of each card
print(f"Your hand is: {first_card["value"]} of {first_card["suit"]}, {second_card["value"]} of {second_card["suit"]}, {third_card["value"]} of {third_card["suit"]}, {fourth_card["value"]} of {fourth_card["suit"]}, {fifth_card["value"]} of {fifth_card["suit"]}")
card_values=[first_card["value"],second_card["value"],third_card["value"],fourth_card["value"],fifth_card["value"]]  
# check if user's drawn five cards iif the same suit
if first_card["suit"]==second_card["suit"]==third_card["suit"]==fourth_card["suit"]==fifth_card["suit"]:
    print(f"Wow! You drew five {first_card["suit"]}!")
# check if user drew a pair [2]
for a,b in itertools.combinations(card_values, 2):
    if a==b:
        print(f"Whoa! You drew a pair of {a}s!")
# check if user has drawn a triple
for a,b,c in itertools.combinations(card_values, 3):
    if a==b==c:
        print(f"Nice! A triple! You drew three {a}s!")
# convert face cards to their numerical values [3]
for i in range(len(card_values)):
    card_values[i]=11 if card_values[i]=="JACK" else card_values[i]
for j in range(len(card_values)):
    card_values[j]=12 if card_values[j]=="QUEEN" else card_values[j]
for k in range(len(card_values)):
    card_values[k]=13 if card_values[k]=="KING" else card_values[k]
for l in range(len(card_values)):
    card_values[l]=1 if card_values[l]=="ACE" else card_values[l]
# convert all card values to integers [4]
c=[int(value) for value in card_values]
# put card values in descending order [5]
v=sorted(c,reverse=True)
# check if user has drawn a straight
for a,b,c,d,e in itertools.combinations(v, 5):
    if a==(b+1) and b==(c+1) and c==(d+1) and d==(e+1):
        print("Sweet! You drew a straight!")
#References:
#[1]https://www.geeksforgeeks.org/python/how-to-parse-nested-json-in-python/
#[2]https://stackoverflow.com/questions/16603282/how-to-compare-each-item-in-a-list-with-the-rest-only-once
#[3]https://stackoverflow.com/questions/44081148/python-replace-string-in-list-with-integer
#[4]https://www.geeksforgeeks.org/python/python-converting-all-strings-in-list-to-integers/
#[5]https://docs.python.org/3/library/functions.html#sorted