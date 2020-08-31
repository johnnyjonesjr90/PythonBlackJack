import random
deck = ["2","3","4","5","6","7","8","9","10","KING","QUEEN","JACK","ACE"]
suit = [ "CLUBS", "SPADES", "HEARTS", "DIAMONDS" ]


def Deal():
    rando= random.choice(deck)
    return rando
      
def Convert(card, total):
            card= Deal()
            trans=0
            if (card == "KING" or card == "QUEEN" or card == "JACK"):
                trans = 10
                return trans

            if (card == "ACE"):
                if (11 + total > 21):
                    trans = 1
                    return trans
                trans = 11
                return trans

            else:
                trans = int(card)
                return trans

def Suitchoice():
            result = random.choice(suit)
            return result;



def HitStay():
        
            return "(1) Hit or (2) Stay?\n\nChoose and then Press Enter";
        
def Bust():
        
            return "Sorry you busted\n\nPress Enter";
        
def Hit21():
        
            return "Congrats!!! you hit 21\n\nPress Enter";
        
