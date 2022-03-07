

from random import shuffle

def createDeck():
    Deck = []

    faceValues = ["A","J","K","Q"]

    for i in range(4): #4 different suits of a card deck
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck


class Player:
    def __init__(self,hand = [],money = 100):
        self.Hand = hand
        self.score = self.setScore()
        self.Money = money
        self.bet = 0

    def __str__(self):
        currentHand = ""
        for card in self.Hand:
            currentHand += str(card) + " "
        finalStaus = currentHand + "score: " + str(self.score)
        return finalStaus

    def setScore(self):
        self.score = 0
        fCardsDict = {"A":11, "J":10, "Q":10, "K":10,
                      "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10}
        aceCounter = 0
        for card in self.Hand:
            self.score += fCardsDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score


    def hit(self,card):
        self.Hand.append(card)
        self.score = self.setScore()

    def play(self,newHand):
        self.Hand = newHand
        self.score = self.setScore()

    def Bet(self,amount):
        self.Money -= amount
        self.bet += amount

    def win(self,result):
        if result == True:
            if self.score == 21 and len(self.Hand) == 2:
                print("Player 1 has a Blackjack!")
                self.Money += 2.5*self.bet
            else:
                self.Money += 2*self.bet
                print("PLayer 1 Wins")
            self.bet = 0
        else:
            self.bet = 0
            print("Computer Wins!")

    def tie(self):
        self.Money += self.bet
        self.bet = 0
        print("Game Tied")

    def hasBjack(self):
        if self.score == 21 and len(self.Hand) == 2:
            return True
        else:
            return False


def printHouse(House):
    for card in range(len(House.Hand)):
        if card == 0:
            print("*", end=" ")
        elif card == len(House.Hand) -1:
            print(House.Hand[card])
        else:
            print(House.Hand[card], end=" ")


cardDeck = createDeck()
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]
player1 = Player(firstHand)
House = Player(secondHand)
cardDeck = createDeck()
print("Money Left: ", player1.Money)

while(True):
    if len(cardDeck) < 20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    player1.play(firstHand)
    House.play(secondHand)
    print("Enter the Keyword 'Exit' anytime to exit the game")
    Bet = (input("Please enter your Bet: "))

    if Bet.upper() == "EXIT":
        if player1.Money > 100:
            print("You came in with 100 and going back with: ",player1.Money)
            print("You made yourself a little rich today!")
        elif player1.Money < 100:
            print("You came in with 100 and going back with: ", player1.Money)
            print("Hard Luck today HUH!")
        else:
            print("You came in with 100 and going back with: ", player1.Money)
            print("You were neutral, nothing gained or lost!")
        break
    else:
        bet = int(Bet)
        player1.Bet(bet)
        printHouse(House)
        print(player1)

        if player1.hasBjack():
            if House.hasBjack():
                player1.tie()
            else:
                player1.win(True)
                print("Player 1 Wins")
        else:
            while(player1.score < 21):
                action = input("Do you want another card?(y/n): ")
                if action == "y":
                    player1.hit(cardDeck.pop())
                    print(player1)
                    printHouse(House)
                else:
                    break
            if player1.score > 21:
                print("Oops, you busted")
                player1.win(False)
            else:
                while(House.score < 16):
                    House.hit(cardDeck.pop())
                    print(House)
                if player1.score > 21:
                    if House.score > 21:
                        player1.tie()
                    else:
                        player1.win(False)
                elif player1.score > House.score:
                    player1.win(True)
                elif player1.score == House.score:
                    player1.tie()
                else:
                    if House.score > 21:
                        player1.win(True)
                    else:
                        player1.win(False)

        print("Money Left: ", player1.Money)
