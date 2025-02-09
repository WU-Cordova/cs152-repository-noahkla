
from datastructures.bag import Bag
import random



class card:
    def __init__(self, suit, num):
        suits = ['\u2660', '\u2665', '\u2666', '\u2663']
        self.n = num
        self.suit = suits[suit]
    def get_value():
        return self.n
    
    def __eq__(self, other):
        if self.n == other[0]and self.suit == suits[other[2]]:
            return True
        return False
    
    def __hash__(self):
        return hash([self.n, self.suit])

class decks:
    def __init__(self, n):
        self.d = Bag()
        
        for i in range(n):
            for j in range(13):
                for x in range(4):
                    self.d.add(card(suit = x, num = j))

    def random_card(self):
        tv = self.d.__len__()
        x = random.randint(1, tv)
        for j in range(13):
                for x in range(4):
                    if [j, x] in self.d:
                        x -= self.d.count([j, x0])
                        if x <=0:
                            return [j, x]
    





class game:
    def __init__(self, n):
        self.deck = decks(n)
        self.p1 = 0
        self.p2 = 0
    
    def play_game():
        return




        
        
def main():
    Bag()
    d = decks(n=1)
    print('foobar')
    print(d.random_card())
    print("Hello, World!")



if __name__ == '__main__':
    main()

