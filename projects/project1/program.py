
from datastructures.bag import Bag
import random



class card:
    def __init__(self, suit, num):
        suits = ['\u2660', '\u2665', '\u2666', '\u2663']
        self.n = num
        self.suit = suits[suit]
    def get_value():
        return self.n

    def print_card(self):
        if self.n >= 2 and self.n <= 10:
            print(str(self.n) + self.suit)
        if self.n == 1:
            print('ace of '+ self.suit)
        if self.n == 11:
            print('Jack of ' + self.suit)
        if self.n == 12:
            print('Queen of ' + self.suit)
        if self.n == 13:
            print('King of ' + self.suit)
    
    def __eq__(self, other):
        suits = ['\u2660', '\u2665', '\u2666', '\u2663']
       # print(other)
        if other == None:
            return False
        try: 
            if self.n == other[0]and self.suit == suits[other[1]]:
                return True
        except:

            if self.n == other.n and self.suit == other.suit:
                return True
        return False
    
    def __hash__(self):
        suits = ['\u2660', '\u2665', '\u2666', '\u2663']
        return hash((self.n, suits.index(self.suit)))
# n is the number of decks to be created
class decks:
    def __init__(self, n):
        self.d = Bag()
        
        for i in range(n):
            for j in range(1, 13):
                for x in range(4):
                    self.d.add(card(suit = x, num = j))

    def random_card(self):
        tv = self.d.__len__()
      #  print('distinct items: '+str(self.d.__len__()))
        n = random.randint(1, tv)
        for j in range(1, 13):
                for x in range(4):
                    if self.d.__contains__((j, x)):
                        n -= self.d.count((j, x))
                       # print(self.d.count((j, x)))
                        if n <=0:
                            self.d.remove((j, x))
                           # print(j, x)
                            return (j, x)
        print('returned nothing')
        print(n)
    




# Creates a game with n decks
class game:
    def __init__(self, n):
        self.deck = decks(n)
        self.p1 = 0
        self.p2 = 0
        self.p1h = Bag()
        self.p2h = Bag()
        for i in range(2):
            c = self.deck.random_card()
            self.p1h.add(card(c[1], c[0]))
            self.p1 += c[0]
          #  print(c[0], self.p1)
            c = self.deck.random_card()
            self.p2h.add(card(c[1], c[0]))
            self.p2 += c[0]
           # print(c[0], self.p2)
        
      #  print(self.deck.d.__len__())
      #  print(self.p1, self.p2)
   #     self.print_game()

    #This function prints out player1's hand and points,  
    # and the commented out part does that for player2
    def print_game(self):
        print('player 1: '+ str(self.p1))
        print('player 1 hand: ')
        for c in self.p1h.distinct_items():
            c.print_card()
        
      #  print('player 2: '+ str(self.p2))
      #  print('player 2 hand: ')
      #  for c in self.p2h.distinct_items():
       #     c.print_card()
    
    def play_game(self):
        while True:
            self.print_game()
            print(' Player 1\'s turn: hit or stay')
            x = input()
            if x == 'hit':
                c = self.deck.random_card()
                c2 = card(c[1], c[0])
                c2.print_card()
                self.p1h.add(c2)
                self.p1 += c[0]
                
            if self.p1 > 21:
                print('Player 1 loses!')
                return
                
            if self.p2 <=11:
                c = self.deck.random_card()
                self.p2h.add(card(c[1], c[0]))
                self.p2 += c[0]
                print('player 2 hit')
                if self.p2 > 21:
                    print('Player 2 loses!')
                    return
            elif x == 'stay' and self.p2 > 11:
                if self.p1 > self.p2:
                    print('Player 1 wins!')
                    
                if self.p2 > self.p1:
                    print('Player 2 wins!')
                    
                if self.p1 == self.p2:
                    print('Tie!')
                    
                return
            
            
            




        
        
def main():
    Bag()
    d = decks(n=1)
    c1 = card(2, 9)
    c2 = card(2, 9)
   # print(c1 == c2)
  #  print('foobar')
  #  print(d.random_card())
   # print("Hello, World!")
    g = game(1)
    g.play_game()
    



if __name__ == '__main__':
    main()

