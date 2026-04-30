"""
Inheritance means inheriting attributes and methods from one class to another class.

To avoid code duplication between classes we use these inheritance concept.

In the below code,

Player->act as parent class

CricketPlayer->acts as child class

TennisPlayer->acts as child class

"""
import datetime
class Player:
    def __init__(self,firstName,lastName,birthYear):
        self.firstName=firstName
        self.lastName=lastName
        self.birthYear=birthYear

    def get_age(self):
        current=datetime.datetime.now()
        return current.year-self.birthYear


class CricketPlayer(Player):
    def __init__(self,firstName,lastName,birthYear):
        super().__init__(firstName,lastName,birthYear)
        self.scores=[]


class TennisPlayer(Player):
    def __init__(self,firstName,lastName,birthYear):
        super().__init__(firstName,lastName,birthYear)
        self.aces=[]

dhoni=CricketPlayer("MS","dhoni",1980)
print(dhoni.get_age())                        


