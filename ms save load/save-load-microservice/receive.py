import requests

BASE = "http://localhost:8000"
game_id = "game"
player_id = "player123"

# Save slot
data = {"levelsCompleted":[1,2],"health":100,"coins":50,"upgrades":{"locked":["double_jump"],"unlocked":["shield"]}}
res = requests.post(f"{BASE}/games/{game_id}/players/{player_id}/save?slotId=slot1", json=data)
print(res.status_code, res.json())

# Load slot
res = requests.get(f"{BASE}/games/{game_id}/players/{player_id}/save?slotId=slot1")
print(res.status_code, res.json())

# Autosave checkpoint
checkpoint = {"levelsCompleted":[1,2,3],"health":90,"coins":100,"upgrades":{"locked":[],"unlocked":["shield","speed_boost"]}}
res = requests.post(f"{BASE}/games/{game_id}/players/{player_id}/checkpoint", json=checkpoint)
print(res.status_code, res.json())