class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
        
    def change_material(self, new_material):
        """Change le matériau de la pièce."""
        self.material = new_material
        
    def __str__(self):
        return f"{self.name} est fait de {self.material}"


class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}  # Dictionnaire privé contenant les pièces
        
    def add_part(self, part):
        """Ajoute une pièce au bateau."""
        self.__parts[part.name] = part
        
    def display_state(self):
        """Affiche toutes les pièces du bateau."""
        if not self.__parts:
            print("Le bateau n'a pas encore de pièces.")
        else:
            for part in self.__parts.values():
                print(part)
    
    def replace_part(self, part_name, new_part):
        """Remplace une pièce existante par une nouvelle."""
        if part_name not in self.__parts:
            print(f"Aucune pièce nommée {part_name} trouvée.")
        else:
            self.__parts[part_name] = new_part
            print(f"La pièce {part_name} a été remplacée par {new_part}.")
            
    def change_part(self, part_name, new_material):
        """Modifie directement le matériau d'une pièce."""
        if part_name not in self.__parts:
            print(f"Aucune pièce nommée {part_name} trouvée.")
        else:
            self.__parts[part_name].change_material(new_material)
            print(f"Le matériau de {part_name} a été changé en {new_material}.")


class Racingship(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed
        self.history = []  # ✅ Ajout d'un historique
        
    def display_speed(self):
        """Affiche la vitesse maximale du bateau de course."""
        print(f"La vitesse maximale de {self.name} est {self.max_speed} km/h.")

    def add_history(self, history):
        """Ajoute un événement à l'historique."""
        self.history.append(history)
        
    def show_history(self):
        """Affiche l'historique des modifications."""
        if not self.history:
            print("Aucun historique n'est disponible.") 
        else:
            for action in self.history:
                print(action)


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
            bateau.add_history(f"Changement du matériau de {part_name} à {new_material}")

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
