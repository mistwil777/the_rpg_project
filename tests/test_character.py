import unittest
from character import Character

class TestCharacter(unittest.TestCase):
    def test_character_creation(self):
        hero = Character("Hero")
        self.assertEqual(hero.name, "Hero")
        self.assertEqual(hero.health, 100)

if __name__ == '__main__':
    unittest.main()