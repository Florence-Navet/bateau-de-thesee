class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
        
    def change_material(self, new_material):
        self.material = new_material
        
    def __str__(self):
        return f"{self.name} est fait de {self.material}"
    

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {} 
        
    def add_part(self, part):
        self.__parts[part.name] = part
        
    def display_state(self):
        if not self.__parts:
            print("Le bateau n'a pas encore de pièces.")
        else:
            for part in self.__parts.values():
                print(part)
    
    def replace_part(self, part_name, new_part):
        if part_name not in self.__parts:
            print(f"Aucune pièce nommée {part_name} trouvée.")
        else:
            self.__parts[part_name] = new_part
            print(f"La pièce {part_name} a été remplacée par {new_part}.")
            
    def change_part(self, part_name, new_material):
        if part_name not in self.__parts:
            print(f"Aucune pièce nommée {part_name} trouvée.")
        else:
            self.__parts[part_name].change_material(new_material)
            print(f"Le matériau de {part_name} a été changé en {new_material}.")
