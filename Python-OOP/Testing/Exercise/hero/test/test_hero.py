from project.hero import Hero
import unittest

class VehicleTests (unittest.TestCase):
    
    def setUp (self):
        self.my_hero = Hero("Kircho", 10, 50.0, 50.0)
        self.enemy_hero = Hero("Pencho", 9, 40.0, 50.0)

    def test_constructor_all_valid (self):
        self.assertEqual(self.my_hero.username, "Kircho")
        self.assertEqual(self.my_hero.level, 10)
        self.assertEqual(self.my_hero.health, 50.0)
        self.assertEqual(self.my_hero.damage, 50.0)

        self.assertEqual(self.enemy_hero.username, "Pencho")
        self.assertEqual(self.enemy_hero.level, 9)
        self.assertEqual(self.enemy_hero.health, 40.0)
        self.assertEqual(self.enemy_hero.damage, 50.0)

    def test_str_dunder (self):
        result_my_hero = self.my_hero.__str__()
        result_enemy_hero = self.enemy_hero.__str__()

        expected_result_my_hero = f"Hero {self.my_hero.username}: {self.my_hero.level} lvl\n" \
            f"Health: {self.my_hero.health}\n" \
                f"Damage: {self.my_hero.damage}\n"
        
        self.assertEqual(result_my_hero, expected_result_my_hero)

        expected_result_enemy_hero = f"Hero {self.enemy_hero.username}: {self.enemy_hero.level} lvl\n" \
            f"Health: {self.enemy_hero.health}\n" \
                f"Damage: {self.enemy_hero.damage}\n"

        self.assertEqual(result_enemy_hero, expected_result_enemy_hero)
    

    def test_battle_same_username_raises (self):
        self.enemy_hero.username = "Kircho"
        with self.assertRaises(Exception) as msg:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), "You cannot fight yourself")

    def test_battle_health_below_or_equal_zero_raises (self):

        self.my_hero.health = 0
        with self.assertRaises(ValueError) as msg:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), "Your health is lower than or equal to 0. You need to rest")

        self.my_hero.health = -1
        with self.assertRaises(ValueError) as msg:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), "Your health is lower than or equal to 0. You need to rest")

        self.my_hero.health = 50.0
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as msg:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")

        self.enemy_hero.health = -1
        with self.assertRaises(ValueError) as msg:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(msg.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")


    def test_battle_draw_less_than_zero (self):
        self.my_hero = Hero("Kircho", 10, 50.0, 50.0)
        self.enemy_hero = Hero("Pencho", 10, 50.0, 50.0)
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(result, "Draw")

    def test_battle_draw_equal_zero (self):
        self.my_hero = Hero("Kircho", 1, 50.0, 50.0)
        self.enemy_hero = Hero("Pencho", 1, 50.0, 50.0)
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(result, "Draw")
    
    def test_battle_self_hero_wins (self):
        self.my_hero = Hero("Kircho", 2, 55.0, 50.0)
        self.enemy_hero = Hero("Pencho", 1, 50.0, 50.0)
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(self.my_hero.level, 3)
        self.assertEqual(self.my_hero.health, 10.0)
        self.assertEqual(self.my_hero.damage, 55.0)
        self.assertEqual(result, "You win")

    def test_battle_enemy_hero_wins (self):
        self.my_hero = Hero("Kircho", 1, 50.0, 50.0)
        self.enemy_hero = Hero("Pencho", 2, 55.0, 50.0)
        result = self.my_hero.battle(self.enemy_hero)
        self.assertEqual(self.enemy_hero.level, 3)
        self.assertEqual(self.enemy_hero.health, 10.0)
        self.assertEqual(self.enemy_hero.damage, 55.0)
        self.assertEqual(result, "You lose")

if __name__ == '__main__':
    unittest.main()