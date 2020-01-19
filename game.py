# file | module import
import player_dice 
from person import Person 

#function to analyse result and display the winner 
def max_num(total_result): 
    win_num =[key for key in total_result.items()] # iterating through result dictionary
    print("\n  THE WINNER!!!\n-------------------") # banner head
    print(max(win_num)) #filtered out the highest number in associated with the player

def main(): # main function of the program
    try: # try program for exception
        person = Person("name", 0) # object created

        # empty list to store player name and score record respectively
        player_names= []
        track_scores = []

        # empty dictionary list one to store each result and then update the total result
        result = {}
        total_result ={} 

        player_names = player_dice.no_of_player(person) #function with created object as parameter
        counter = len(player_names) # counter to store number of players

        print("\n  TAKE TURN TO ROLL DICE\n-------------------------") #banner head
        for cnt in range(0, counter): # iterate through number of players while taking turn to roll dice
            person.score = player_dice.roll_dice(cnt + 1, 6) #call to function to roll dice
            track_scores.append(person.score) # each dice number stored on list
            result = {player_names[cnt]:track_scores[cnt]} #each player record store on dictionary list 
            total_result.update(result) # final result dictionary list updated

        print("\n  DICE RESULT\n----------------") # banner head
        for value, key in total_result.items(): # iterate through dictionary list to fetch the key, value pairs
            print("{} : {}".format(value, key)) # format to display the player record
        max_num(total_result) # function call to display the winner, player with highest number
        print("\n")
    except: #main except to catch any other exception or error that might arise
        print("...... Exit application and restart game") # message display incase of exception

main() # call to execute the program