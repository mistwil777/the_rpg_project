import unittest
from character import
def test_attack(self):
    hero = Character("Hero", 100)
    enemy = Character("Enemy", 100)
    hero.attack(enemy)
    self.assertEqual(enemy.health, 90)
    
    
if __name__ == '__main__':
    unittest.main()