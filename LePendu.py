"""
Mohamed HABBAAINA, le 20 oct 2022
Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
jeu le pendu dans le terminal.
Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
niveau.
Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
ici, et afficher :
- Le nombre de vies restantes au joueur
- Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
En expert, la liste n’apparaîtra pas)
- Des “_” pour remplacer les lettres non trouvées
- Les lettres proposées qui se trouvent dans le mot
La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.
"""

import random
# def length(liste):
#     nbr = 0
#     for i in liste :
#         nbr = nbr + 1
#     return nbr

mots = [""]

with open ("dico_france.txt","r", encoding="ISO-8859-1") as f:
    for l in f:
        mots.append(l.rstrip("\n"))
mot = random.choice(mots)
# print(mot)
# nbr_lettre = length(list(mot))
# #print (nbr_lettre)

choix = int(input ("choisissez votre niveau : \n 1 debutant \n 2 intermediaire \n 3 expert \n1, 2 ou 3 ? "))

if choix == 1:
    
    tentatives = 10

    affichage = ""
    for l in mot:
        affichage = affichage + "_ "

    lettres_trouvees = ""

    while tentatives>0:
        print("Mot à deviner : ", affichage)
        proposition = input("proposez une lettre : ")
        if proposition in mot:
            lettres_trouvees = lettres_trouvees + proposition
            print("-> Bien vu!")
        else:
            tentatives = tentatives - 1
            print("-> Nope. Il vous reste", tentatives, "tentatives")

        affichage = ""
        for x in mot:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print(">>> Gagné! <<<")
            break
    print("    * Fin de la partie *    ")

elif choix == 2 :
    tentatives = 7

    affichage = ""
    for l in mot:
        affichage = affichage + "_ "

    lettres_trouvees = ""

    while tentatives>0:
        print("Mot à deviner : ", affichage)
        proposition = input("proposez une lettre : ")
        if proposition in mot:
            lettres_trouvees = lettres_trouvees + proposition
            print("-> Bien vu!")
        else:
            tentatives = tentatives - 1
            print("-> Nope. Il vous reste", tentatives, "tentatives")

        affichage = ""
        for x in mot:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print(">>> Gagné! <<<")
            break
    print("    * Fin de la partie *    ")

elif choix == 3 :
    tentatives = 4

    affichage = ""
    for l in mot:
        affichage = affichage + "_ "

    lettres_trouvees = ""

    while tentatives>0:
        print("Mot à deviner : ", affichage)
        proposition = input("proposez une lettre : ")
        if proposition in mot:
            lettres_trouvees = lettres_trouvees + proposition
            print("-> Bien vu!")
        else:
            tentatives = tentatives - 1
            print("-> Nope. Il vous reste", tentatives, "tentatives")

        affichage = ""
        for x in mot:
            if x in lettres_trouvees:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print(">>> Gagné! <<<")
            break
    print("    * Fin de la partie *    ")

else:
    print ("nous n'avons pas compris votre choix")