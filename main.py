from classes import Racingship, Part, Ship

def menu():
    print("\nMENU :")
    print("1. Afficher l'état du bateau")
    print("2. Remplacer une pièce")
    print("3. Modifier le matériau d'une pièce")
    print("4. Afficher la vitesse maximale")
    print("5. Afficher l'historique")
    print("6. Quitter")

def main():
    bateau = Racingship("Le Merry", 100)
    bateau.add_part(Part("La coque", "bois"))
    bateau.add_part(Part("Le gouvernail", "fer"))
    bateau.add_part(Part("Canon", "acier"))

    while True:
        menu()  # ✅ Afficher le menu à chaque tour
        choix = input("Votre choix : ")  # ✅ Demander le choix de l'utilisateur

        if choix == "1":
            bateau.display_state()
        
        elif choix == "2":
            part_name = input("Nom de la pièce à remplacer : ")
            new_part_name = input("Nom de la nouvelle pièce : ")
            new_part_material = input("Matériau de la nouvelle pièce : ")
            new_part = Part(new_part_name, new_part_material)
            bateau.replace_part(part_name, new_part)
            bateau.add_history(f"La pièce {part_name} a été remplacée par {new_part}.")

        elif choix == "3":
            part_name = input("Nom de la pièce dont vous voulez modifier le matériau : ")
            new_material = input("Nouveau matériau : ")
            bateau.change_part(part_name, new_material)
            bateau.add_history(f"Changement du matériau de {part_name} en {new_material}")

        elif choix == "4":
            bateau.display_speed()

        elif choix == "5":
            bateau.show_history()

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")

if __name__ == "__main__":
    main()
