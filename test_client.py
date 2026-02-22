"""Use external requests library to make an HTTP POST request for testing."""

import json
import requests

BASE_URL = "http://127.0.0.1:5000"


def print_result(name: str, response: requests.Response) -> None:
    print(f"TEST: {name}")
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print("Response JSON:")
        print(json.dumps(data))
    except ValueError:
        print("Not JSON response body:")
        print(response.text)
    print()


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
    print_result("Save progress data", resp)


def test_load():
    """valid load request after save"""
    resp = requests.get(
        f"{BASE_URL}/games/FireSTORM/players/player1/save",
        params={"slotId": "slot1"},
    )
    print_result("Load progress data", resp)
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
    print_result("gameId unknown", resp)


if __name__ == "__main__":
    print("Calling Save/Load microservice test cases\n")
    test_save()
    test_load()
    test_unknown_gameId()