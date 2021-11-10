# revue des concepts de programmation
# 2021-11-09
# contexte - menu de choix

# CONSTANTES
TITRE = "Menu alimentaire"
BEAUTIFUL = " | "

# Liste
menu = ["pomme", "biscuit", "chocolat","pizza", "hamburger"]

#Affichage du menu
print("Bienvenu à notre restaurant gratuit!! Voici le menu.")
print(BEAUTIFUL + TITRE + BEAUTIFUL)
print()
for i in range(0, len(menu)) :
    print(f"{i} - {menu[i]}")

print("")

#Prise de décision
code=True
while code == True:
    choix=input("Quelle est votre choix alimentaire? ").lower()
    if choix == menu[0] or choix == "0":
        print("Bien sur. Voici votre", menu[0],".")
    elif choix == menu[1] or choix == "1":
        print("Bien sur. Voici votre", menu[1], ".")
    elif choix== menu[2] or choix == "2":
        print("Bien sur. Voici votre", menu[2], ".")
    elif choix == menu[3] or choix == "3":
        print("Bien sure. Voici votre", menu[3], ".")
    elif choix == menu[4] or choix == "4":
        print("Bien sure. Voici votre", menu[4], ".") 
    else:
        print("Choix invalide") 


#Démande l'utilisateur si ils sont satisfait
    print("")
    print("Êtes-vous satisfaits avec votre choix? oui ou non")
    réponse=input().lower()
   
 
    if réponse == "oui":
        print("Merci pour votre clientèle. À la prochaine.")
        code=False
        
    elif réponse == "non":
        print("S'il vous plaît choisisser encore.")
        code=True
    
    else:
        print("Choix invalide")

# Fin du menu