from datetime import datetime

class Day():
    def __init__(self, name):
        self.name = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
class Week(Day):
    def __init__(self, amount):
        self.amount = 7
class Employe():
    def __init__(self, name, exp, preference):
        self.name = name
        self.exp = exp
        self.preference = preference

ref = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
# Scheduler est l'algorithme qui recoit l'horaire initial vide ainsi
# qu'une liste d'employes avec les preferences des employes
# Retourne l'horaire avec le nombre de shift chaque jour
# Doit avoir minimum 2 shifts par jour
def Scheduler(schedule, employes):
    for i in range(employes.length):
        for j in range(4):
            schedule[employes[i].preference[j]] += 1
    return schedule


employe1 = Employe("Dwight",  3, ["monday", "tuesday", "wednesday", "thursday"])
employe2 = Employe("Jim",     1, ["tuesday", "wednesday", "thursday", "friday"])
employe3 = Employe("Pam",     2, ["wednesday", "thursday", "friday", "saturday"])
employe4 = Employe("Micheal", 4, ["thursday", "friday", "saturday", "sunday"])
    
schedule = {"monday": 0, "tuesday":0,"wednesday":0, "thursday":0, "friday":0, "saturday":0, "sunday":0}
employes = [employe1, employe2, employe3, employe4]
print(employes.count)
#print(Scheduler(schedule, employes))
