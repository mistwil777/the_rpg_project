import unittest
from character import Character

def test_take_damage(self):
    hero = Character("Hero", 100)
    hero.take_damage(20)
    self.assertEqual(hero.health, 80)
    
    
if __name__ == '__main__':
    unittest.main()