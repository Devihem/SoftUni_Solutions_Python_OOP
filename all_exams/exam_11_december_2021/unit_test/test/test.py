from oop.all_exams.exam_11_december_2021.unit_test.project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team_empty = Team("EMPTYTEAM")
        self.team_test = Team("TEST")
        self.team_test.add_member(Name1=23, Name2=25)

    def test_empty_team_data(self):
        self.assertEqual('EMPTYTEAM', self.team_empty.name)
        self.assertEqual({}, self.team_empty.members)

    def test_name_is_alpha(self):
        with self.assertRaises(ValueError) as error:
            Team("GO GO")
        self.assertEqual('Team Name can contain only letters!', str(error.exception))

    def test_name_is_alpha_2(self):
        with self.assertRaises(ValueError) as error:
            Team("9GAG")
        self.assertEqual('Team Name can contain only letters!', str(error.exception))

    def test_add_member_proper(self):
        result = self.team_empty.add_member(Name1=23, Name2=25)
        self.assertEqual({'Name1': 23, 'Name2': 25}, self.team_empty.members)
        self.assertEqual('Successfully added: Name1, Name2', result)

    def test_add_member_that_already_exist(self):
        result = self.team_empty.add_member(Name1=20, Name2=21)
        self.assertEqual({'Name1': 20, 'Name2': 21}, self.team_empty.members)
        self.assertEqual('Successfully added: Name1, Name2', result)

    def test_add_member_empty(self):
        result = self.team_empty.add_member()
        self.assertEqual({}, self.team_empty.members)
        self.assertEqual('Successfully added: ', result)

    def test_remove_member_correct(self):
        result = self.team_test.remove_member("Name1")
        self.assertEqual('Member Name1 removed', result)
        self.assertEqual({'Name2': 25}, self.team_test.members)

    def test_remove_member_no_such_name(self):
        result = self.team_test.remove_member("Name3")
        self.assertEqual('Member with name Name3 does not exist', result)
        self.assertEqual({'Name1': 23, 'Name2': 25}, self.team_test.members)

    def test_method_gt(self):
        result = self.team_test > self.team_empty
        self.assertEqual(True, result)

        # Reverse
        result = self.team_empty > self.team_test
        self.assertEqual(False, result)

        # Test same
        result = self.team_empty > Team("TestA")
        self.assertEqual(False, result)

    def test_len_dunder(self):
        result = len(self.team_test)
        result1 = len(self.team_empty)
        self.assertEqual(2, result)
        self.assertEqual(0, result1)

    def test_add_dunder(self):
        result = self.team_empty + self.team_test
        self.assertEqual("EMPTYTEAMTEST", result.name)
        self.assertEqual({'Name1': 23, 'Name2': 25}, result.members)

    def test_str_dunder(self):
        result = str(self.team_test)
        result1 = str(self.team_empty)
        self.assertEqual("Team name: TEST\nMember: Name2 - 25-years old\nMember: Name1 - 23-years old", result)
        self.assertEqual("Team name: EMPTYTEAM", result1)


if __name__ == "__main__":
    main()
