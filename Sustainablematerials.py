# Define materials and structure classes
class Material:
    def __init__(self, name, sustainable):
        self.name = name
        self.sustainable = sustainable

class Structure:
    def __init__(self, name, required_materials):
        self.name = name
        self.required_materials = required_materials
        self.is_built = False

    def build(self, player):
        # Check if player has all sustainable materials
        for material, qty_needed in self.required_materials.items():
            if player.inventory.get(material, 0) < qty_needed or not material.sustainable:
                print(f"Cannot build {self.name}. Missing or non-sustainable materials.")
                return False
        # Deduct materials from player inventory
        for material, qty_needed in self.required_materials.items():
            player.inventory[material] -= qty_needed
        self.is_built = True
        print(f"{self.name} successfully built!")
        return True

# Define the Quest class
class Quest:
    def __init__(self, title, description, structures):
        self.title = title
        self.description = description
        self.structures = structures
        self.completed = False

    def check_completion(self):
        if all(structure.is_built for structure in self.structures):
            self.completed = True
            print("Quest Completed: All structures built!")
            # Reward the player here
            return True
        return False

# Define the Player class
class Player:
    def __init__(self):
        self.inventory = {}  # Inventory should be a dictionary of Material: Quantity pairs

    def gather_material(self, material, quantity):
        if material.name in self.inventory:
            self.inventory[material] += quantity
        else:
            self.inventory[material] = quantity
        print(f"Gathered {quantity} units of {material.name}")

# Instantiate sustainable materials
wood = Material("Sustainable Wood", sustainable=True)
stone = Material("Eco-Friendly Stone", sustainable=True)

# Instantiate structures
windmill = Structure("Windmill", {wood: 10, stone: 5})
barn = Structure("Barn", {wood: 15, stone: 10})

# Create the quest
sustainable_building_quest = Quest(
    title="Sustainable Building Quest",
    description="Construct a windmill and barn using only sustainable materials.",
    structures=[windmill, barn]
)

# Sample Gameplay
player = Player()

# Player gathers materials
player.gather_material(wood, 20)
player.gather_material(stone, 20)

# Attempt to build each structure
windmill.build(player)
barn.build(player)

# Check if quest is completed
sustainable_building_quest.check_completion()
