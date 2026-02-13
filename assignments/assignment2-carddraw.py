# Card Draw
# Author: Sylvia Chapman Kent
# Draws two cards from a shuffled deck and prints the value and suit of each

import requests
import json
#get shuffled deck
url1="https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response1=requests.get(url1)
deck=response1.json()
#record deck id
deck_id=deck["deck_id"]
#draw 2 cards from shuffled deck
url2=(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2")
response2=requests.get(url2)
draw=response2.json()
#record details of both cards [1]
first_card=draw['cards'][0]
second_card=draw['cards'][1]
#print value and suit of each card
print(first_card["value"],first_card["suit"],second_card["value"],second_card["suit"])
# to do: check if user has drawn pair triple straight or all same suit and congratulate them

#References:
#[1]https://www.geeksforgeeks.org/python/how-to-parse-nested-json-in-python/