#Revue de python pour le cour ICS4U
#11-09-2021
#Samir Serhal

#Définition des noms dans le système
TITRE = "Menu Alimentaire"
Fancy = "|"

#Affichage de bienvenue et introduction au  menu
print("Bienvenue à notre restaurant")
print(Fancy,TITRE,Fancy)
print("")
#Les choix alimentaires
a = "pomme"
b = "biscuit"
c = "chocolat"

menu = [a, b, c]

print("Il y a",len(menu),"choix dans le menu.")
print("Les choix sont:")


#for i in range (0, len(menu)):
#   print("")
#    print("{i} - {menu(i)}")

print(a)
print(b)
print(c)

print("Quelle est votre choix?")
choix=input().lower()
print("Vous avez choisi", choix)
