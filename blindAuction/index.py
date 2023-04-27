import os
import sys
from art import logo
print(logo)
print('Welcome to the secret auction program.')

biddersLeft = 'yes'
bidders = {}

while biddersLeft == 'yes':

    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    biddersLeft = input("Are there any other bidders? Type 'yes' or 'no'.")
    os.system('clear')

    if biddersLeft == 'no':
        highBid = -sys.maxsize - 1
        for bidder in bidders:
            if bidders[bidder] > highBid:
                highBidder = bidder
                highBid = bidders[bidder]
        
        print(f"The winner is {highBidder} with a bid of ${highBid}")
