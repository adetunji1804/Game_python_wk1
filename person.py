
'''
    a class Person define with two properties, initializer / constructor, 
    output format and a function to get player name
'''
class Person: # class name

    def __init__(self, name, score = 0): # initializer | constructor
        self.name = name # value returned to name property
        self.score = score # value returned to score property

    def __str__(self): # output format function
        return f"\n {self.name} :{self.score}\n"

    def player_name(self, id): #function to prompt for player name
        self.name = input("Name of player " + str(id) + ": ")
        return self.name

