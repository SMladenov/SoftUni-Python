from project.soccer_player import SoccerPlayer

import unittest

class SoccerPlayerTests (unittest.TestCase):

    def setUp(self):
        self.player = SoccerPlayer('Goshko', 18, 7, 'Juventus')  

    def test_constructor_all_valid (self):
        self.assertEqual(self.player.name, 'Goshko')
        self.assertEqual(self.player.age, 18)
        self.assertEqual(self.player.goals, 7)
        self.assertEqual(self.player.team, 'Juventus')
        self.assertEqual(self.player.achievements, {})

    def test_name_invalid_throw (self):
        with self.assertRaises(ValueError) as msg:
            SoccerPlayer('Gosh', 18, 7, 'Juventus')
        self.assertEqual(str(msg.exception), "Name should be more than 5 symbols!")
    
    def test_age_invalid_throw (self):
        with self.assertRaises(ValueError) as msg:
            SoccerPlayer('Goshko', 15, 7, 'Juventus')
        self.assertEqual(str(msg.exception), "Players must be at least 16 years of age!")

    def test_goals_below_zero (self):
        player2 = SoccerPlayer('Goshko', 18, -5, 'Juventus')
        self.assertEqual(player2.goals, 0)

    def test_team_invalid_throw (self):
        with self.assertRaises(ValueError) as msg:
            SoccerPlayer('Goshko', 18, -5, 'Mladost')
        self.assertEqual(str(msg.exception), "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!")


    def test_change_team_invalid (self):
        result = self.player.change_team("Mladost")
        self.assertEqual(result, "Invalid team name!")

    def test_change_team_success (self):
        result = self.player.change_team("PSG")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "PSG")

    def test_add_new_achievement (self):
        result = self.player.add_new_achievement("Nacepih se")
        self.assertEqual(result, f"Nacepih se has been successfully added to the achievements collection!")
        self.assertTrue("Nacepih se" in self.player.achievements.keys())
    
    def test_lt_player1 (self):
        player1 = SoccerPlayer('Goshko3', 20, 10, 'Barcelona')
        player2 = SoccerPlayer('Goshko2', 18, 8, 'Juventus')

        result1 = player1 < player2
        self.assertEqual(result1, f"Goshko3 is a better goal scorer than Goshko2.")

    def test_lt_player2 (self):
        player1 = SoccerPlayer('Goshko3', 20, 10, 'Barcelona')
        player2 = SoccerPlayer('Goshko2', 18, 8, 'Juventus')

        result1 = player1 > player2
        self.assertEqual(result1, f"Goshko3 is a top goal scorer! S/he scored more than Goshko2.")

if __name__ == '__main__':
    unittest.main()
