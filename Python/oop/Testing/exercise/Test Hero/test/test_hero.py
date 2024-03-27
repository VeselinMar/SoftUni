from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Ivan", 1, 100, 100)
        self.enemy_hero = Hero("Chris", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("Ivan", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)
        self.assertEqual("Chris", self.enemy_hero.username)
        self.assertEqual(1, self.enemy_hero.level)
        self.assertEqual(50, self.enemy_hero.health)
        self.assertEqual(50, self.enemy_hero.damage)

    def test_battle_fight_same_username_raiseException(self):
        with self.assertRaises(Exception) as ex:
            self.enemy_hero.username = "Ivan"
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_fight_without_health(self):
        with self.assertRaises(ValueError) as ve:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_fight_enemy_no_health(self):
        with self.assertRaises(ValueError) as ve:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual(str(ve.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")

    def test_battle_with_result_draw_returns_draw_and_decreases_health_on_both_players(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy_hero.health)
        self.assertEqual(0, self.hero.health)

    def test_battle_with_result_win_returns_win_increases_level_health_damage_of_hero(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_with_result_lose_returns_lose_increases_level_health_damage_of_enemy(self):
        self.enemy_hero.health = 105
        self.enemy_hero.damage = 100
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(2, self.enemy_hero.level)
        self.assertEqual(10, self.enemy_hero.health)
        self.assertEqual(105, self.enemy_hero.damage)

    def test_str_username_level_health_damage(self):
        self.assertIn(str(self.hero.username), self.hero.__str__())
        self.assertIn(str(self.hero.level), self.hero.__str__())
        self.assertIn(str(self.hero.health), self.hero.__str__())
        self.assertIn(str(self.hero.damage), self.hero.__str__())


if __name__ == "__main__":
    main()
