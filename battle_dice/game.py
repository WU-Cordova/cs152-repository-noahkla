import random
from character import Character

class Game:
    def __init__(self, player1: Character, player2: Character) -> None:
        """ Constructor for the Game class. Sets the players to instance variables.
        Args:   
            player1 (Character): The first player.
            player2 (Character): The second player.
        """
        self.player1 = player1
        self.player2 = player2
        

    def attack(self, attacker: Character, defender: Character) -> None:
        """ Attacks the defender. Algorithm: 
            1. Roll a random number between 1 and 6 for the attack.
            2. Subtract the attack value from the defender's health.
            3. If the defender's health is less than or equal to 0, they are defeated.
            4. Print the result of the attack.
        Args:
            attacker (Character): The attacker.
            defender (Character): The defender. 
        """
        v = random.randint(1, 6)*attacker.attack_power
        defender.health -= v
       
        print(attacker.name+' attacked '+defender.name+' for '+str(v)+' damage, '+defender.name+' is at '+str(defender.health)+' health')
        if defender.health <= 0:
            print(defender.name + ' is defeated!')
    def start_battle(self) -> None:
        """ Starts the battle between the two players. Algorithm: 
            1. While both players are alive, do the following:
                1.1. Player 1 attacks Player 2.
                1.2. If Player 2 is defeated, break the loop.
                1.3. Player 2 attacks Player 1.
                1.4. If Player 1 is defeated, break the loop.
            2. Print the result of the battle.
        """
        while True:
            self.attack(self.player1, self.player2)
            if self.player2.health <=0:
                break

            self.attack(self.player2, self.player1)
            if self.player1.health <=0:
                break
