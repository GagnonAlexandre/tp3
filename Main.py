# tp3
#alexandre gagnon 401 
Dans ce code, tu devras affronter des adversaires avec des points de vies.
Si vos points de vies sont superieures, vous gagnez. Si ils sont inferieurs, vous perdez
Lorsque tu perds tout tes vies, tu perds"""
import random
niveau_vie = 20
jouer = True
nbr_victoires = 0
while jouer:
    valeur_monstre = random.randint(1, 12)
    print("\n"
          "Vous tombez face à face avec un adversaire de difficulté:", valeur_monstre, )
    print("Vous avez un niveau de vie de ", niveau_vie, )
    print("Que voulez-vous faire ?")
    print("1- Combattre cet adversaire")
    print("2- Contourner cet adversaire et aller ouvrir une autre porte")
    print("3- Afficher les règles du jeu")
    print("4- Quitter la partie")
    choix = input()
    if choix == "1":
        valeur_dee_1 = random.randint(0, 6)
        valeur_dee_2 = random.randint(0, 6)
        valeur_total = valeur_dee_1 + valeur_dee_2
        print("Si votre dé a une valeur plus grosse que celle du monstre, vous gagnez cette ronde.")
        print("Vous avez rouler une valeur de ", valeur_dee_1," et ", valeur_dee_2, )
        print("Vous avez une valeur totale de ", valeur_total, )
        if valeur_dee_1 + valeur_dee_2  > valeur_monstre:
            print("Vous avez battu le monstre!\n Il vous reste maintenant", niveau_vie, " vies\n")
            nbr_victoires += 1
            if nbr_victoires == 3:
                print("Felecitation, vous avex gagner 3 fois. Vous avez maintenant pas le choix mais d'affronter le boss")
                valeur_dee_1 = random.randint(0, 6)
                valeur_dee_2 = random.randint(0, 6)
                valeur_dee_3 = random.randint(0, 6)
                valeur_total_2 = valeur_dee_1 + valeur_dee_2 + valeur_dee_3
                valeur_boss = random.randint(14, 18)
                print("Vous roulez maintenant 3 dees. Le boss a  ", valeur_boss, " vies")
                print("Votre premier dee a une valeur de ", valeur_dee_1, )
                print("Votre deuxieme a une valeur de ", valeur_dee_2, )
                print("Votre troisieme a une valeur de ", valeur_dee_3, )
                print("Vous avez une valeur de ", valeur_total_2, )
                if valeur_total_2 > valeur_boss:
                    print("Vous avez gagner contre le boss. Felicitation!")
                    niveau_vie -= 3
                elif valeur_total_2 < valeur_boss:
                    print("Vous avez perdu contre le boss. Vous perdez 3 vies.")
                    niveau_vie -= 3

        elif valeur_dee_1 + valeur_dee_2 < valeur_monstre:
            print("Le monstre vous a battu!")
            niveau_vie -=1
            print("Il vous reste maintenant", niveau_vie, " vies")
    elif choix == "2":
        print("D'accords, cela vous coutera un point de vie")
        niveau_vie -= 1
        print("Il vous reste maintenant", niveau_vie," vies")
    elif choix == "3":
        print("Vous allez faire face a plusieurs adversaires\n"
              "Chacuns des adversaires ont un niveau de difficulte\n"
              "Vous devez rouler des dees et si votre valeur est plus grande que la force de l'adversaire, vous gagnez.\n"
              "Si vous pensiez que l'adversaire est trop fort, vous pouvez le contourner et aller ouvrir une autre porte.\n"
              "Mais cela vous coutera un point de vie\n"
              "Vous commencez avec 20 point de vies.\n"
              "Lorsque vous perdez contre un monstre, vous en perdez 2.\n"
              "Mais, si vous quittez, vous en perdez 1.")
    elif choix == "4":
        jouer = False
    if niveau_vie == 0:
        #le joueur est poche et il est mort
        print("Vous avez perdus toutes vos vies, vous avez perdus")
        jouer = False
