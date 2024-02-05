def zombie_adventure():
    print("Bienvenue dans l'aventure de survie zombie !")
    print("Vous êtes dans une école infestée de zombies. Deux couloirs s'offrent à vous.")
    print("1. Explorer le couloir de gauche")
    print("2. Courir vers le couloir de droite")

    health = 100  # Points de vie initiaux
    choice = input("Quel couloir choisissez-vous ? (1/2) : ")

    if choice == "1":
        print("Vous trouvez une salle de classe sécurisée avec des provisions.")
        print("Vous entendez du bruit. Voulez-vous enquêter ?")
        print("1. Enquêter sur le bruit")
        print("2. Rester caché et silencieux")
        second_choice = input("Votre choix ? (1/2) : ")

        if second_choice == "1":
            print("C'était un autre survivant ! Vous avez maintenant un allié.")
        elif second_choice == "2":
            print("Vous restez en sécurité mais seul. La survie continue.")
        else:
            print("Choix non valide. Les zombies vous surprennent. Vous perdez des points de vie.")
            health -= 30  # Perte de points de vie en cas de choix invalide

    elif choice == "2":
        print("Malheureusement, vous tombez sur un groupe de zombies ! Vous perdez des points de vie.")
        health -= 50  # Perte de points de vie en cas de rencontre avec des zombies
    else:
        print("Choix non valide. Les zombies vous attrapent. Fin de l'aventure.")
        return

    print(f"Points de vie restants : {health}")

    if health <= 0:
        print("Vos points de vie ont atteint zéro. Vous n'avez pas survécu.")
    else:
        print("Félicitations, vous avez survécu à l'infestation de zombies!")
        print("Vous trouvez une sortie sécurisée, mais votre aventure n'est pas encore terminée.")

        print("Que voulez-vous faire maintenant?")
        print("1. Chercher d'autres survivants")
        print("2. Trouver un abri permanent")
        print("3. Explorer d'autres zones")

        final_choice = input("Votre choix ? (1/2/3) : ")

        if final_choice == "1":
            print("Vous trouvez un groupe de survivants. Ensemble, vous augmentez vos chances de survie.")
        elif final_choice == "2":
            print("Vous découvrez un abri solide. C'est maintenant votre refuge sûr.")
        elif final_choice == "3":
            print("En explorant d'autres zones, vous découvrez des ressources précieuses pour votre survie.")
        else:
            print("Choix non valide. Votre aventure continue avec de nouveaux défis.")

# Lancer le jeu
zombie_adventure()

