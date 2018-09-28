import random
num = []
suite = []
Player1 = []
Player2 = []
stack = []
round = 0
wars = 0

class CardOperations:
    def MakeCards(self):
        global num,suite
        num = ['1','2','3','4','5','6','7','8','9','10','11','12', '13']
        suite = ['H', 'C', 'D', 'S']


    def ShufandAllot(self):
        for x in suite:
            random.shuffle(num)
            for c in num:
                if (num.index(c))%2==0:
                    Player1.append(c)
                else:
                    Player2.append(c)
            '''print("Suite :" + x)
            print("Player 1")
            print(Player1)
            print("Player 2")
            print(Player2)
'''

    def deal(self):
        while (len(Player1) != 0 and len(Player2) != 0):
                global round, wars
                round+=1
                p1 = Player1.pop(0)
                p2 = Player2.pop(0)
                if p1 > p2:
                    Player1.append(p1)
                    Player1.append(p2)
                if p2 > p1:
                    Player2.append(p1)
                    Player2.append(p2)
                else:
                    wars +=1
                    p1w1 = Player1.pop(0)
                    p1w2 = Player1.pop(0)
                    p1w3 = Player1.pop(0)

                    p2w1 = Player2.pop(0)
                    p2w2 = Player2.pop(0)
                    p2w3 = Player2.pop(0)

                    if(p1w1+p1w2+p1w3)>(p2w1+p2w2+p2w3):
                        Player1.extend((p1,p2,p1w1,p1w2,p1w3,p2w1,p2w2,p2w3))
                    else:
                        Player2.extend((p1, p2, p1w1, p1w2, p1w3, p2w1, p2w2, p2w3))
        if (len(Player1) == 0):
            winner = "Computer"
        if (len(Player2) == 0):
            winner = "You"
        return(winner)









obj = CardOperations()
obj.MakeCards()
obj.ShufandAllot()
print("The game has been won by:")
print(obj.deal())
print("Rounds :")
print(round)
print("Wars :")
print(wars)
