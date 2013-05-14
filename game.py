# Rock-paper-scissors-lizard-Spock

import random

rock = 0
Spock = 1
paper = 2
lizard = 3
scissors = 4

# helper functions

def number_to_name(number):
    if (number == rock):
        return 'rock'
    elif number == Spock:
        return 'Spock'
    elif number == paper:
        return 'paper'
    elif number == lizard:
        return 'lizard'
    elif number == scissors:
        return 'scissors'

def name_to_number(name):
    if len(name) > 0:
        if (name.lower() == 'rock'):
            return rock
        elif name.lower() == 'spock':
            return Spock
        elif name.lower() == 'paper':
            return paper
        elif name.lower() == 'lizard':
            return lizard
        elif name.lower() == 'scissors':
            return scissors

def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
    
    print 'Player chooses ' + name
    print 'Computer chooses ' + number_to_name(comp_number)
    
    winner = player_number - comp_number
    if (winner % 5) == 1 or (winner % 5) == 2:
        print "Player wins!\n"
    elif (player_number - comp_number) % 5 == 0:
        print "Player and computer tie!\n"
    else:    
        print "Computer wins!\n"
        

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


