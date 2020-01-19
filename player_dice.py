# import module
from person import Person
import random

def no_of_player(Person): # function to process the number of players
    try: # try exception within this function
        player_list = [] # empty player list declared
        number = int(input("Enter number of players: ")) #prompt for number of players
        for num in range(number): # iterate through the number of player
            player_list.append(Person.player_name(num + 1)) #associate unique number to each player
        return player_list # function return player list
    except:
         print("invalid!!! Please input integer number") # message display if exception occur


def roll_dice(tag, no_of_time = 6): # function to roll dice
    try: # try exception within the function
        no_of_time = int(input(" Auto roll dice, player ("+ str(tag) +"): " )) # prompt number of times to roll dice
        return random.randint(1, no_of_time) # return the result of rolled dice
    except:
        print("invalid Number! You're disqualified") # message displayed if exception occur