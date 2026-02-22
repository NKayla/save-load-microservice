"""Use external requests library to make an HTTP POST request for testing."""

import json
import requests

BASE_URL = "http://127.0.0.1:5000"


def test_save():
    """Valid save request with the progress data."""
    data = {
        "coins": 350,
        "levelCompleted": 3
    }
    resp = requests.post(
        f"{BASE_URL}/games/FireSTORM/players/player1/save",
        params={"slotId": "slot1"},
        json=data,
    )
    print("Save progress data", resp.status_code)
    print("Body:", resp.json())


def test_load():
    """valid load request after save"""
    resp = requests.get(
        f"{BASE_URL}/games/FireSTORM/players/player1/save",
        params={"slotId": "slot1"},
    )
    print("Load progress data", resp)
    data = resp.json()
    print("coins:", data["coins"])
    print("levelCompleted:", data["levelCompleted"])


def test_unknown_gameId():
    """Save with a GameId that is not valid."""
    data = {
            "coins": 350,
            "levelCompleted": 3
    }
    resp = requests.post(
        f"{BASE_URL}/games/unknowngame/players/player1/save",
        json=data,
    )
    print("gameId unknown", resp.status_code)
    print("Unknown:", resp.json())


if __name__ == "__main__":
    print("Calling Save/Load microservice test cases\n")
    test_save()
    test_load()
    test_unknown_gameId()