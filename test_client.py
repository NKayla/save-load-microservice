import unittest
import service
from service import app


class TestSave(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        service.saves = {}  # reset

    def test_save_default(self):
        res = self.client.post(
            "/games/game1/players/player1/save",
            json={"levelCompleted": 5, "coins": 215}
        )
        self.assertEqual(res.status_code, 201)

    def test_load(self):
        # first save
        self.client.post(
            "/games/game1/players/player1/save",
            json={"levelCompleted": 3, "coins": 150}
        )
        res = self.client.get("/games/game1/players/player1/save")
        self.assertEqual(res.status_code, 200)

        res_data = res.get_json()
        self.assertEqual(res_data["levelCompleted"], 3)
        self.assertEqual(res_data["coins"], 150)

    def test_load_not_found(self):
        res = self.client.get("/games/game1/players/player1/save?slotId=notfound")
        self.assertEqual(res.status_code, 404)

    def test_save_none(self):
        res = self.client.post("/games/game1/players/player1/save",
                               content_type="application/json"
                               )
        self.assertEqual(res.status_code, 400)


if __name__ == "__main__":
    unittest.main()