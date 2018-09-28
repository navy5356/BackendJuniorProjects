import random


class player:
    deck = []
    name = ""

    def __init__(self, name):
        self.name = name

    def shuffle(self):
        random.shuffle(self.deck)


class card:
    facevalue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []

    def makedeck(self):
        for j in range(4):
            for i in range(13):
                self.deck.append(self.facevalue[i])
        random.shuffle(self.deck)


class game:
    numberofrounds = 0
    numberofwars = 0
    winner = 0
    playerdeck = []
    computerdeck = []
    def __init__(self):
        self.setup()

    def setup(self):
        cards = card()
        cards.makedeck()
        name = input("Enter the Name of the Player ")
        print("\n")
        Player1 = player(name)
        Computer = player("Computer")

        for i in range(26):
            Player1.deck = cards.deck[: 26]
            Computer.deck = cards.deck[26: 52]

        Player1.shuffle()
        Computer.shuffle()
        self.playerdeck = Player1.deck
        self.computerdeck = Computer.deck
        self.playername = Player1.name

    def playgame(self):
        while self.playerdeck != [] and self.computerdeck != []:
            self.numberofrounds = self.numberofrounds + 1
            if self.playerdeck[0] > self.computerdeck[0]:
                buffer1 = self.playerdeck[0]
                buffer2 = self.computerdeck[0]
                self.playerdeck = self.playerdeck[1:]
                self.playerdeck.append(buffer1)
                self.playerdeck.append(buffer2)
                self.computerdeck = self.computerdeck[1:]

            elif self.playerdeck[0] < self.computerdeck[0]:
                buffer2 = self.playerdeck[0]
                buffer1 = self.computerdeck[0]
                self.computerdeck = self.computerdeck[1:]
                self.computerdeck.append(buffer1)
                self.computerdeck.append(buffer2)
                self.playerdeck = self.playerdeck[1:]
            else:
                if len(self.playerdeck) >= 4 and len(self.computerdeck) >= 4:
                    self.numberofwars = self.numberofwars + 1
                    playersum = self.playerdeck[1] + self.playerdeck[2] + self.playerdeck[3]
                    computersum = self.computerdeck[1] + self.computerdeck[2] + self.computerdeck[3]
                    if playersum > computersum:
                        buffer0 = self.playerdeck[0]
                        buffer1 = self.playerdeck[1]
                        buffer2 = self.playerdeck[2]
                        buffer3 = self.playerdeck[3]
                        buffer01 = self.computerdeck[0]
                        buffer11 = self.computerdeck[1]
                        buffer21 = self.computerdeck[2]
                        buffer31 = self.computerdeck[3]
                        self.playerdeck = self.playerdeck[4:]
                        self.playerdeck.append(buffer0)
                        self.playerdeck.append(buffer1)
                        self.playerdeck.append(buffer2)
                        self.playerdeck.append(buffer3)
                        self.playerdeck.append(buffer01)
                        self.playerdeck.append(buffer11)
                        self.playerdeck.append(buffer21)
                        self.playerdeck.append(buffer31)
                        self.computerdeck = self.computerdeck[4:]

                    elif (playersum < computersum):
                        buffer01 = self.playerdeck[0]
                        buffer11 = self.playerdeck[1]
                        buffer21 = self.playerdeck[2]
                        buffer31 = self.playerdeck[3]
                        buffer0 = self.computerdeck[0]
                        buffer1 = self.computerdeck[1]
                        buffer2 = self.computerdeck[2]
                        buffer3 = self.computerdeck[3]
                        self.computerdeck = self.computerdeck[4:]
                        self.computerdeck.append(buffer0)
                        self.computerdeck.append(buffer1)
                        self.computerdeck.append(buffer2)
                        self.computerdeck.append(buffer3)
                        self.computerdeck.append(buffer01)
                        self.computerdeck.append(buffer11)
                        self.computerdeck.append(buffer21)
                        self.computerdeck.append(buffer31)
                        self.playerdeck = self.playerdeck[4:]

                    else:
                        self.playerdeck = self.playerdeck[4:]
                        self.computerdeck = self.computerdeck[4:]

                else:
                    if len(self.playerdeck) >= 4:
                        self.winner = "player"
                        break
                    elif len(self.computerdeck) >= 4:
                        self.winner = "computer"
                        break


        print("Number of Rounds held: " + str(self.numberofrounds))
        print("Number of Wars held: " + str(self.numberofwars))
        if self.playerdeck == [] or self.winner == "computer":
            print("The Computer Won the Game")
        if self.computerdeck == [] or self.winner == "player":
            print(str(self.playername) + " Won the Game")


Game = game()
Game.playgame()

