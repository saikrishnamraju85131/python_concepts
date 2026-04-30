import datetime
class CricketPlayer:
    def __init__(self,firstName,lastName,birthYear):
        self.firstName=firstName
        self.lastName=lastName
        self.birthYear=birthYear
        self.scores=[]

    def get_age(self):
        current=datetime.datetime.now()#it returns an object which consists year,month,date  hours,minutes,seconds,microseconds
        #calculating age
        return current.year - self.birthYear


class TennisPlayer:
    def __init__(self,firstName,lastName,birthYear):
        self.firstName=firstName
        self.lastName=lastName
        self.birthYear=birthYear
        self.aces=[]#no.of aces in a match
    def get_age(self):
        current=datetime.datetime.now()
        return current.year-self.birthYear

#creating cricket player object     
virat=CricketPlayer("virat","kholi",1980)
print(virat.get_age())        

#creating tennis player object
roger=TennisPlayer("m","roger",1978)
print(roger.get_age())

"""
In above code we can clearly observe attribute and method duplication between CricketPlayer class and TennisPlayer class.

The solution for this attribute and method duplication is "Inheritance".

"""