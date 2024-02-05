import time  # Import the time module for a better user experience

def print_with_pause(text, pause_time=1.5):
    print(text)
    time.sleep(pause_time)

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        choice = input("Votre choix ? ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Choix non valide. Veuillez entrer un numéro valide.")

def zombie_adventure():
    print_with_pause("Bienvenue dans l'aventure de survie zombie !")
    print_with_pause("Vous êtes dans une école infestée de zombies. Deux couloirs s'offrent à vous.")

    choices = ["Explorer le couloir de gauche", "Courir vers le couloir de droite"]
    choice_index = make_choice("Quel couloir choisissez-vous ?", choices)

    health = 100  # Points de vie initiaux

    if choice_index == 1:
        print_with_pause("Vous trouvez une salle de classe sécurisée avec des provisions.")
        print_with_pause("Vous entendez du bruit. Voulez-vous enquêter ?")

        options_second_choice = ["Enquêter sur le bruit", "Rester caché et silencieux"]
        second_choice_index = make_choice("Votre choix ?", options_second_choice)

        if second_choice_index == 1:
            print_with_pause("C'était un autre survivant ! Vous avez maintenant un allié.")
        elif second_choice_index == 2:
            print_with_pause("Vous restez en sécurité mais seul. La survie continue.")
        else:
            print_with_pause("Choix non valide. Les zombies vous surprennent. Vous perdez des points de vie.")
            health -= 30  # Perte de points de vie en cas de choix invalide

    elif choice_index == 2:
        print_with_pause("Malheureusement, vous tombez sur un groupe de zombies ! Vous perdez des points de vie.")
        health -= 50  # Perte de points de vie en cas de rencontre avec des zombies
    else:
        print_with_pause("Choix non valide. Les zombies vous attrapent. Fin de l'aventure.")
        return

    print_with_pause(f"Points de vie restants : {health}")

    if health <= 0:
        print_with_pause("Vos points de vie ont atteint zéro. Vous n'avez pas survécu.")
    else:
        print_with_pause("Félicitations, vous avez survécu à l'infestation de zombies!")
        print_with_pause("Vous trouvez une sortie sécurisée, mais votre aventure n'est pas encore terminée.")

        print("Que voulez-vous faire maintenant?")
        options_final_choice = ["Chercher d'autres survivants", "Trouver un abri permanent", "Explorer d'autres zones"]
        final_choice_index = make_choice("Votre choix ?", options_final_choice)

        if final_choice_index == 1:
            print_with_pause("Vous trouvez un groupe de survivants. Ensemble, vous augmentez vos chances de survie.")
        elif final_choice_index == 2:
            print_with_pause("Vous découvrez un abri solide. C'est maintenant votre refuge sûr.")
        elif final_choice_index == 3:
            print_with_pause("En explorant d'autres zones, vous découvrez des ressources précieuses pour votre survie.")
        else:
            print_with_pause("Choix non valide. Votre aventure continue avec de nouveaux défis.")

# Lancer le jeu
zombie_adventure()
