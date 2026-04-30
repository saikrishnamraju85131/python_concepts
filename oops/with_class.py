#doing player analysis using class and object
class player:
    def __init__(self,first,last,scores):
        self.firstName=first
        self.lastName=last
        self.scores=scores
    def get_average(self):
        return sum(self.scores)/len(self.scores)    
    
    def add_score(self,score):
        self.scores.append(score)

    def get_score(self):
        return self.scores  
    
    #operator overloading
    def __lt__(self,other):
        return self.get_average() < other.get_average()

    def __eq__(self, other):
        return self.get_average()== other.get_average()

          


virat=player("virat","kohli",[20,30,0])
print(virat.get_average())
dhoni=player("Ms","dhoni",[30,40,50])
print(dhoni.get_average())
print(virat<dhoni)
print(virat==dhoni)
