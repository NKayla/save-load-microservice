from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

saves = {}

def current_timestamp():
    return datetime.now().isoformat()


# POST: save progress
@app.route("/games/<gameId>/players/<playerId>/save", methods=["POST"])
def save_game(gameId, playerId):
    slotId = request.args.get("slotId", "default")
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Save data missing or invalid JSON"}), 400

    # add time
    data["lastSaved"] = current_timestamp()

    saves[(gameId, playerId, slotId)] = data

    return jsonify({
        "message": f"Save stored successfully in slot '{slotId}'",
        "status": 201
    }), 201


# POST: autosave
@app.route("/games/<gameId>/players/<playerId>/checkpoint", methods=["POST"])
def checkpoint(gameId, playerId):
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Checkpoint data missing or invalid"}), 400

    slotId = "autosave"
    data["lastSaved"] = current_timestamp()
    saves[(gameId, playerId, slotId)] = data

    return jsonify({
        "message": "Checkpoint saved successfully",
        "status": 201
    }), 201


# GET: load save data
@app.route("/games/<gameId>/players/<playerId>/save", methods=["GET"])
def load_game(gameId, playerId):
    slotId = request.args.get("slotId", "default")
    data = saves.get((gameId, playerId, slotId))

    if not data:
        return jsonify({"error": f"Save slot '{slotId}' not found"}), 404

    return jsonify(data), 200



# GET: list save slots for a player
@app.route("/games/<gameId>/players/<playerId>/save-slots", methods=["GET"])
def list_slots(gameId, playerId):
    player_saves = {slot: val for (g,p,slot), val in saves.items() if g==gameId and p==playerId}
    if not player_saves:
        return jsonify({"message": "No saves found"}), 204
    return jsonify(player_saves), 200



# DELETE: remove a save slot
@app.route("/games/<gameId>/players/<playerId>/save", methods=["DELETE"])
def delete_save(gameId, playerId):
    slotId = request.args.get("slotId", "default")
    key = (gameId, playerId, slotId)
    if key in saves:
        del saves[key]
        return jsonify({"message": f"Slot '{slotId}' deleted successfully"}), 200
    return jsonify({"error": f"Slot '{slotId}' not found"}), 404


# Run
if __name__ == "__main__":
    app.run(debug=True, port=8000)