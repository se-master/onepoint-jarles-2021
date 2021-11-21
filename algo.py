from datetime import datetime
import json

class Employe():
    def __init__(self, name, preference):
        self.name = name
        self.preference = preference

ref_jours = ["monday", "tuesday","wednesday", "thursday", "friday", "saturday", "sunday"]
# Scheduler est l'algorithme qui recoit l'horaire initial vide ainsi
# qu'une liste d'employes avec les preferences des employes
# Retourne l'horaire avec le nombre de shift chaque jour
# Doit avoir minimum 2 shifts par jour
def Scheduler(schedule, employes):
    for i in range(len(employes)):
        for j in range(4):
            schedule[employes[i].preference[j]] += 1
    return schedule

with open('test.json') as f:
    data = json.load(f)
    print(data['name'])


schedule = {"monday": 0, "tuesday":0,"wednesday":0, "thursday":0, "friday":0, "saturday":0, "sunday":0}

#print(Scheduler(schedule, employes))

#print(Scheduler(schedule, employes), file=open("output.txt", "a"))
#print("\nAllez voir output.txt pour voir le résultat! :)")
