# save-load-microservice

This microservice handles the persistent storage and retrieval of a player's game state progress. It provides a REST API over HTTP for storing and retrieving progress data in order to load to game by using optional save slots or autosave. 
- Python 3 and Flask. 

## Install
```
git clone https://github.com/NKayla/save-load-microservice.git
cd save-load-microservice
```

Install dependencies 
```
pip install flask
```

## Running the Microservice 
```
python service.py
```

## Testing
1. Run service.py
2. Test with browser in separate terminal.
```
python test_client.py
```


## Parameters:
- `gameId`  Unique Id for game.
- `playerId` Unique Id for player.
- `slotId` Unique Id for save slot assigned to player. (Query parameter)

## Data Format
Data is sent and received as JSON. Examples:
- levelsCompleted [array of integers]
- coins [int]
- upgrades [boolean]


## How to REQUEST data 
Saving the game state (player progress) - send data to service.
- Method: POST
- Endpoint: `/games/{gameId}/players/{playerId}/save?slotId=slot2`
- URL to call endpoint (local dev): http://localhost:5000
- Content-Type: application/json
- Status Codes: 200 Created, 400 Bad Request 

Example JSON Body:
```json
{
  "levelsCompleted": [1, 2, 3],
  "health": 90, 
  "coins": 320,
  "upgrades": {
    "locked": false,
    "unlocked": true
}
```

## Example request 
```
import requests

# save progress 
response = requests.post(
    "http://127.0.0.1:5000/games/game1/players/player81/save",
    params={"slotId: "default"},
    json={"levelCompleted": 5, "coins": 350}
}

print("Status", response.status_code)
print("Body":, response.json())
```

## How to RECEIVE data 
Retrieve the player's progress from service.
- Method: GET
- Endpoint: `/games/{gameId}/players/{playerId}/save?slotId=slot2`
- URL to call endpoint (local dev): http://localhost:5000
- Status Codes: 200 Ok, 404 Not Found

Example
```
import requests

response = requests.get(
  "http://127.0.0.1:5000/games/game1/players/player81/save",
  params={"slotId: "default"}
}

print("Status", response.status_code)
print("Body":, response.json())
```

Response body example (game client receives):
```json
{
  "levelsCompleted": [1, 2, 3],
  "health": 90, 
  "coins": 320,
  "upgrades": {
    "locked": false,
    "unlocked": true
}
```


## Autosave
Autosave used in game to save at checkpoints. 
Method: POST
- Autosave is controlled by the game client.
- Normal http request.







## UML Sequence Diagram: 
