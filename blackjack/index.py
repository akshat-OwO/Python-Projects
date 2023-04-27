cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
wantToPlay = 'y'

def showScore(deck, score, peek):
    print(f'\tYour cards: {deck}, current score: {score}')
    print(f"\tComputer's first card: {peek[0]}")

def finalScore(yourDeck, yourScore, computerDeck, computerScore):
    print(f"\tYour final hand: {yourDeck}, final score: {yourScore}")
    print(f"\tComputer's final hand: {computerDeck}, final score: {computerScore}")

while wantToPlay == 'y':
    wantToPlay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if wantToPlay == 'n':
        exit()
    import os, random
    os.system('clear')

    from art import logo
    print(logo)
    
    yourDeck = []
    yourScore = 0
    computerDeck = []
    computerScore = 0
    for i in range(2):
        yourDeck.append(cards[random.randint(0, 12)])
        yourScore += yourDeck[i]
        computerDeck.append(cards[random.randint(0, 12)])
        computerScore += computerDeck[i]

    showScore(yourDeck, yourScore, computerDeck)

    getCard = input("Type 'y' to get another card, type 'n' to pass: ")
    while getCard == 'y':
        if getCard == 'y':
            yourDeck.append(cards[random.randint(0, 12)])
            yourScore += yourDeck[-1]
                
            showScore(yourDeck, yourScore, computerDeck)
            if yourScore > 21:
                finalScore(yourDeck, yourScore, computerDeck, computerScore)
                print('You went over. You lose 😢')
                break
            else:
                getCard = input("Type 'y' to get another card, type 'n' to pass: ")

    if getCard == 'n':
        if computerScore > yourScore:
            finalScore(yourDeck, yourScore, computerDeck, computerScore)
            print('You lose 😢')
        if yourScore > computerScore:
            finalScore(yourDeck, yourScore, computerDeck, computerScore)
            print('You win 😄')