from datetime import datetime
import json

class Day():
    def __init__(self, name):
        self.name = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
class Week(Day):
    def __init__(self, amount):
        self.amount = 7
class Employe():
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference

ref = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
# Scheduler est l'algorithme qui recoit l'horaire initial vide ainsi
# qu'une liste d'employes avec les preferences des employes
# Retourne l'horaire avec le nombre de shift chaque jour
# Doit avoir minimum 2 shifts par jour
def Scheduler(schedule, employes):
    for i in range(len(employes)):
        for j in range(4):
            schedule[employes[i].preference[j]] += 1
    return schedule


with open("dat.txt", "r") as f:
    f.seek(0)
    data = []
    for line in f:
        data.append(line.splitlines())

    limit = int(len(data)/2)
    days = []
    for i in range(limit):
        days.append(str(data[2*i+1]).replace("[","").replace("]","").replace("'","").split(','))
    employes = []
    for i in range(limit):
            employes.append(Employe(str(data[2*i]), days[i]))


schedule = {"monday": 0, "tuesday":0,"wednesday":0, "thursday":0, "friday":0, "saturday":0, "sunday":0}
#print(Scheduler(schedule, employes))
print(Scheduler(schedule, employes), file=open("output.txt", "a"))
