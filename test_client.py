import unittest
from service import app


class TestSave(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.saves = {}

    def test_save_default(self):
        res = self.client.post(
            "/games/game1/players/player1/save",
            json={"levelCompleted": 5, "coins": 215}
        )
        self.assertEqual(res.status_code, 201)

        res_data = res.get_json()
        self.assertIn("player_progress", res_data)
        self.assertEqual(res.get_json()["player_progress"]["levelCompleted"], 5)
        self.assertEqual(res.get_json()["player_progress"]["coins"], 215)

    def test_load(self):
        # first save
        self.client.post(
            "/games/game1/players/player1/save",
            json={"levelCompleted": 3, "coins": 150}
        )
        res = self.client.get("/games/game1/players/player1/save")
        self.assertEqual(res.status_code, 200)

        res_data = res.get_json()
        self.assertIn("player_progress", res_data)
        self.assertEqual(res.get_json()["player_progress"]["levelCompleted"], 3)
        self.assertEqual(res.get_json()["player_progress"]["coins"], 215)


if __name__ == "__main__":
    unittest.main()