class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Armor(Item):
    def __init__(self, name, description, item_armor):
        super().__init__(name, description)
        self.item_armor = item_armor

class Weapon(Item):
    def __init__(self, name, description, item_damage):
        super().__init__(name, description)
        self.item_damage = item_damage

class Potion(Item):
    def __init__(self, name, description, duration, effect_value):
        super().__init__(name, description)
        self.effect_value = effect_value