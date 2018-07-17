'''
    Author: Gavin Andrews
    Date: 4/26/18
    
    Description:
    The function of this program is to create an RPG
    by using the Fighter class. The RPG uses two Fighters
    that attack eachother in combat and calculates the
    HP of each Fighter at the end of the rounds.
    '''

import random

class Fighter:
    
    def __init__(self, name):
        '''
        This function initializes self and name and sets
        a name attribute to the value of the name parameter
        and sets a hit_points attribute to 10.
        
        self: first parameter for every function
        name: the name of a fighter
        '''
        
        self.name = name
        self.hit_points = 10

    def __repr__(self):
        '''
        This function returns a string with the name
        of the fighter and the HP.

        self: Fighter that calls the method
        '''

        return self.name + " " + "(HP: " + str(self.hit_points) + ")"

    def take_damage(self, damage_amount):
        '''
        This function is to decrease the hit_points and
        prints the Fighter's status and points remaining.
        
        self: Fighter that calls the method
        damage_amount: the amount of damage
        '''

        self.hit_points = self.hit_points - damage_amount

        if self.hit_points <= 0:
            print("\tAlas, " + self.name + " has fallen!")
        else:
            print("\t" + self.name + " has " + str(self.hit_points) + " hit points remaining.")

        return None
    
    def attack(self, other):
        '''
        This function is to initiate the attacks between Fighters
        with random damage.
        
        self: Fighter that calls the method
        other: other Fighter being attacked by self
        '''

        print(self.name + " attacks " + other.name + "!")

        attacked = random.randrange(1, 20)
        
        if attacked >= 12:
            damage = random.randrange(1, 6)
            print("\tHits for " + str(damage) + " hit points!")
            other.take_damage(damage)
        else:
            print("\tMisses!")
        
        return None
        
    def is_alive(self):
        '''
        This function is check if the Fighter is alive or dead.
        
        self: Fighter that calls the method
        '''
        
        if self.hit_points > 0:
            return True
        else:
            return False

#==========================================================

def combat_round(first_fighter, second_fighter):
    '''
    This function is the engage the first and second Fighter
    into combat.
    
    first_fighter: the first Fighter to attack
    second_fighter: the second Fighter to attack
    '''
    
    first = random.randrange(1, 6)
    second = random.randrange(1, 6)

    if first == second:
        print("Simultaneous!")
        first_fighter.attack(second_fighter)
        second_fighter.attack(first_fighter)
    elif first > second:
        first_fighter.attack(second_fighter)
        if second_fighter.is_alive():
            second_fighter.attack(first_fighter)
    else:
        second_fighter.attack(first_fighter)
        if first_fighter.is_alive():
            first_fighter.attack(second_fighter)

    return None

#==========================================================

def main():
    '''
    The function of main() is to call the Fighter class and
    plays the game
    
    '''

    Death_Mongrel = Fighter("Death_Mongrel")
    Hurt_then_Pain = Fighter("Hurt_then_Pain")

    i = 1
    while(Death_Mongrel.is_alive() and Hurt_then_Pain.is_alive()):
        print("=" * 19 + " ROUND " + str(i), "=" * 19)
        print(Death_Mongrel)
        print(Hurt_then_Pain)
        
        input("Enter to Fight!")
        
        combat_round(Death_Mongrel, Hurt_then_Pain)
        
        if not Death_Mongrel.is_alive() or not Hurt_then_Pain.is_alive():
            break
        
        i += 1
    
    print("The battle is over!")
    print(Death_Mongrel)
    print(Hurt_then_Pain)

if __name__ == '__main__':
    main()
