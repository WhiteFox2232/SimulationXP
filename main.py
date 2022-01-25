import random
print("\n")
print("||   / |  / /                                            //   / /")
print("||  /  | / /     / __       ( )   __  ___     ___       //___         ___")
print("|| / /||/ /     //   ) )   / /     / /      //___) )   / ___        //   ) ) \\ / /")
print("||/ / |  /     //   / /   / /     / /      //         //           //   / /   \/ /")
print("|  /  | /     //   / /   / /     / /      ((____     //           ((___/ /    / / \n")

print("Bienvenue sur cet outil console Python développé par WhiteFox et permettant de faire une simulation d'xp MEE6")
formatTemps = str(input("Veuillez écrire \"h\" si vous souhaitez exprimer un temps en heures et \"m\" si vous souhaitez exprimer un temps en minutes"))

if formatTemps == "h":
    Temps = int(input("Veuillez entrer le nombre d'heures de discussion :  "))
    Temps *= 60

else:
    Temps = int(input("Veuillez entrer le nombre de minutes de discussion :  "))


globalXP = 0

for i in range(0, Temps):
    xp = random.randint(15, 25)
    globalXP += xp

print("En se basant sur {} minutes de discussion, l'xp gagnée sera potentiellemen de {} xp".format(Temps, globalXP))



