class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def take_damage(self, amount):
        self.health -= amount
        
    def attack(self, target):
        target.take_damage(10)