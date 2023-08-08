from hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):

    def test_entry_data(self):
        # hero [Name:Str , Level:Int , Hp:Int ,Power:Int]
        the_best = Hero("Roronoa Zoro", 100, 2000, 1000)
        self.assertEqual("Roronoa Zoro", the_best.username)
        self.assertEqual(100, the_best.level)
        self.assertEqual(2000, the_best.health)
        self.assertEqual(1000, the_best.damage)

    def test_battle_with_same_hero_name(self):
        the_best = Hero("Roronoa Zoro", 100, 2000, 1000)
        enemy_hero = Hero("Roronoa Zoro", 100, 2000, 1000)
        with self.assertRaises(Exception) as error:
            the_best.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_with_zero_hp(self):
        the_best = Hero("Roronoa Zoro", 100, 0, 1000)
        enemy_hero = Hero("Vinsmkoe Sanji", 100, 2000, 999)
        with self.assertRaises(ValueError) as error:
            the_best.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_with_enemy_with_zero_hp(self):
        the_best = Hero("Roronoa Zoro", 100, 2000, 1000)
        enemy_hero = Hero("Vinsmkoe Sanji", 100, 0, 999)
        with self.assertRaises(ValueError) as error:
            the_best.battle(enemy_hero)
        self.assertEqual(f"You cannot fight Vinsmkoe Sanji. He needs to rest", str(error.exception))

    def test_battle_draw(self):
        the_best = Hero("Roronoa Zoro", 10, 2000, 200)
        enemy_hero = Hero("Vinsmkoe Sanji", 10, 2000, 200)
        result = the_best.battle(enemy_hero)
        self.assertEqual(f"Draw", result)

    def test_battle_win(self):
        the_best = Hero("Roronoa Zoro", 10, 2001, 200)
        enemy_hero = Hero("Vinsmkoe Sanji", 10, 2000, 200)
        result = the_best.battle(enemy_hero)
        self.assertEqual(f"You win", result)
        self.assertEqual(11, the_best.level)
        self.assertEqual(6, the_best.health)
        self.assertEqual(205, the_best.damage)

    def test_battle_lose(self):
        the_best = Hero("Roronoa Zoro", 10, 2000, 200)
        enemy_hero = Hero("Vinsmkoe Sanji", 10, 2001, 200)
        result = the_best.battle(enemy_hero)
        self.assertEqual(f"You lose", result)
        self.assertEqual(11, enemy_hero.level)
        self.assertEqual(6, enemy_hero.health)
        self.assertEqual(205, enemy_hero.damage)

    def test_str_return(self):
        the_best = Hero("Roronoa Zoro", 100, 2000, 1000)
        result = str(the_best)
        self.assertEqual("Hero Roronoa Zoro: 100 lvl\nHealth: 2000\nDamage: 1000\n", result)


if __name__ == "__main__":
    main()
