from flask import Flask, request, jsonify

app = Flask(__name__)

# store saves
saves = {}

ALLOWED_GAMES = {"FireSTORM", "game1"}

# ---------- Save Progress------------
@app.route("/games/<gameId>/players/<playerId>/save", methods=["POST"])
def save_game(gameId, playerId):
    if gameId not in ALLOWED_GAMES:
        return jsonify({"error": f"Unknown '{gameId}'"}), 400

    slotId = request.args.get("slotId", "default")

    player_progress = request.json
    # wrong Id
    if not player_progress:
        return jsonify({"error": "Save data not found"}), 400

    # store Ids in dictionary
    saves[(gameId, playerId, slotId)] = player_progress

    return jsonify({"message": f"Save stored in slot '{slotId}'"}), 200


# --------- Load ------------
@app.route("/games/<gameId>/players/<playerId>/save", methods=["GET"])
def load_game(gameId, playerId):
    if gameId not in ALLOWED_GAMES:
        return jsonify({"error": f"Unknown '{gameId}'"}), 400
    # default if no slot provided
    slotId = request.args.get("slotId", "default")

    player_progress = saves.get((gameId, playerId, slotId))
    if player_progress is None:
        return jsonify({"error": "Save data not found"}), 404

    return jsonify(player_progress), 200


if __name__ == "__main__":
    app.run(debug=True)