import time

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

def explore_left_corridor():
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
        return 30  # Perte de points de vie en cas de choix invalide
    return 0

def run_right_corridor():
    print_with_pause("Malheureusement, vous tombez sur un groupe de zombies ! Vous perdez des points de vie.")
    return 50  # Perte de points de vie en cas de rencontre avec des zombies

def zombie_adventure():
    print_with_pause("Bienvenue dans l'aventure de survie zombie !")
    print_with_pause("Vous êtes dans une école infestée de zombies. Deux couloirs s'offrent à vous.")

    choices = ["Explorer le couloir de gauche", "Courir vers le couloir de droite"]
    choice_index = make_choice("Quel couloir choisissez-vous ?", choices)

    health = 100  # Points de vie initiaux

    if choice_index == 1:
        health -= explore_left_corridor()

    elif choice_index == 2:
        health -= run_right_corridor()

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
            print_with_pause("Le groupe vous informe qu'il existe une cache d'armes non loin d'ici.")
            print_with_pause("Voulez-vous y aller?")
            options_weapon_cache = ["Oui, allons à la cache d'armes", "Non, restons avec le groupe"]
            weapon_cache_choice = make_choice("Votre choix ?", options_weapon_cache)

            if weapon_cache_choice == 1:
                print_with_pause("Vous atteignez la cache d'armes et trouvez des armes puissantes.")
                print_with_pause("Votre groupe est maintenant mieux équipé pour affronter les zombies.")
            elif weapon_cache_choice == 2:
                print_with_pause("Vous restez avec le groupe. La survie continue avec de nouveaux défis.")
            else:
                print_with_pause("Choix non valide. Vous décidez de rester avec le groupe pour la survie.")

        elif final_choice_index == 2:
            print_with_pause("Vous découvrez un abri solide. C'est maintenant votre refuge sûr.")
            print_with_pause("Vous avez le choix de renforcer les défenses de l'abri ou d'explorer les environs.")
            options_shelter = ["Renforcer les défenses de l'abri", "Explorer les environs"]
            shelter_choice = make_choice("Votre choix ?", options_shelter)

            if shelter_choice == 1:
                print_with_pause("En renforçant les défenses, vous repoussez avec succès une attaque zombie.")
                print_with_pause("Votre abri devient plus sûr, mais de nouveaux défis vous attendent.")
            elif shelter_choice == 2:
                print_with_pause("En explorant les environs, vous découvrez une source d'eau potable.")
                print_with_pause("Cela renforce vos réserves, mais soyez prêt pour de nouveaux dangers.")
            else:
                print_with_pause("Choix non valide. L'aventure continue avec de nouveaux défis.")

        elif final_choice_index == 3:
            print_with_pause("En explorant d'autres zones, vous découvrez des ressources précieuses pour votre survie.")
            print_with_pause("Vous trouvez également des signes d'une communauté de survivants.")
            print_with_pause("Voulez-vous les rejoindre?")
            options_join_community = ["Oui, rejoignons la communauté", "Non, continuons en solitaire"]
            join_community_choice = make_choice("Votre choix ?", options_join_community)

            if join_community_choice == 1:
                print_with_pause("Vous rejoignez la communauté et contribuez à sa prospérité.")
                print_with_pause("Ensemble, vous avez de meilleures chances de reconstruire une société.")
            elif join_community_choice == 2:
                print_with_pause("Vous continuez en solitaire, bravant les dangers du monde post-apocalyptique.")
                print_with_pause("Votre aventure individuelle vous réserve de nouveaux défis.")
            else:
                print_with_pause("Choix non valide. Vous prenez votre propre chemin dans ce monde dévasté.")

        else:
            print_with_pause("Choix non valide. Votre aventure continue avec de nouveaux défis.")

# Lancer le jeu
zombie_adventure()
