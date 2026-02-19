# save-load-microservice

This microservice handles the persistent storage and retrieval of a player's game state progress. It provides a REST API over HTTP for storing and retrieving progress data in order to load to game by using optional save slot or autosave. This microservice uses Python 3 and Flask. 

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
python server.py
```

## Testing
1. Run server.py
2. Test with browser in separate terminal.
```
python test_client.py
```


## Parameters:
- `gameId`  Unique Id for game.
- `playerId` Unique Id for player.
- `slotId` Unique Id for save slot assigned to player. 


## How to REQUEST data 
Saving the game state (player progress) - send data to server.
- Method: POST
- Endpoint: /games/{gameId}/players/{playerId}/save?slotId=slot2
- Status Codes: 200 OK, 400 Bad Request 

Example body:
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


## How to RECEIVE data 
Retrieve the player's progress from server.
- Method: GET
- Endpoint: /games/{gameId}/players/{playerId}/save?slotId=slot2
- Status Codes: 200 Ok, 404 Not Found

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
- Autosave is controleld by the game client.
- Normal http request to save. 







## UML Sequence Diagram: 
