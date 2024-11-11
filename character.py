class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self, target):
        target.take_damage(10)