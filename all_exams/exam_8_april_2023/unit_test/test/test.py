from oop.all_exams.exam_8_april_2023.unit_test.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.t_player1 = TennisPlayer("Mario", 26, 6)
        self.t_player2 = TennisPlayer("Luigi", 26, 6.1)
        self.t_player2.add_new_win("Stage 8-4")

    def test_empty_entry(self):
        self.assertEqual("Mario", self.t_player1.name)
        self.assertEqual(26, self.t_player1.age)
        self.assertEqual(6, self.t_player1.points)
        self.assertEqual([], self.t_player1.wins)

    def test_props_name_value_error(self):
        with self.assertRaises(ValueError) as error:
            TennisPlayer("ML", 20, 0)
        self.assertEqual("Name should be more than 2 symbols!", str(error.exception))

    def test_props_name_value_error_2(self):
        with self.assertRaises(ValueError) as error:
            TennisPlayer("M", 20, 0)
        self.assertEqual("Name should be more than 2 symbols!", str(error.exception))

    def test_props_age_value_error_1(self):
        with self.assertRaises(ValueError) as error:
            TennisPlayer("Name", 17, 0)
        self.assertEqual("Players must be at least 18 years of age!", str(error.exception))

    def test_props_age_value_error_2(self):
        with self.assertRaises(ValueError) as error:
            TennisPlayer("Name", -1, 0)
        self.assertEqual("Players must be at least 18 years of age!", str(error.exception))

    def test_props_age_3(self):
        player = TennisPlayer("Name", 18, 0)
        self.assertEqual(18, player.age)

    def test_add_new_win_1(self):
        self.t_player1.add_new_win("minbuldun")
        self.assertEqual(['minbuldun'], self.t_player1.wins)
        self.t_player1.add_new_win("wimbledon")
        self.assertEqual(['minbuldun', 'wimbledon'], self.t_player1.wins)

    def test_add_new_win_2(self):
        result = self.t_player2.add_new_win("Stage 8-4")
        self.assertEqual("Stage 8-4 has been already added to the list of wins!", result)

    def test_dunder_lt_1(self):
        result = self.t_player1.__lt__(self.t_player2)
        self.assertEqual("Luigi is a top seeded player and he/she is better than Mario", result)

    def test_dunder_lt_2(self):
        result = self.t_player2.__lt__(self.t_player1)
        self.assertEqual("Luigi is a better player than Mario", result)

    def test_dunder_str_1(self):
        result1 = str(self.t_player1)
        result2 = str(self.t_player2)

        t_player_3 = TennisPlayer("Name", 100, 20.37)
        t_player_3.add_new_win("Win1")
        t_player_3.add_new_win("Win2")
        t_player_3.add_new_win("Win3")

        result3 = str(t_player_3)

        self.assertEqual('Tennis Player: Mario\nAge: 26\nPoints: 6.0\nTournaments won: ', result1)
        self.assertEqual('Tennis Player: Luigi\nAge: 26\nPoints: 6.1\nTournaments won: Stage 8-4', result2)
        self.assertEqual('Tennis Player: Name\nAge: 100\nPoints: 20.4\nTournaments won: Win1, Win2, Win3', result3)


if __name__ == "__main__":
    main()
