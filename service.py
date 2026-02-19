from flask import Flask, request, jsonify

app = Flask(__name__)

# store saves
saves = {}

# ----------Save------------
@app.route("/games/<gameId>/players/<playerId>/save", methods=["POST"])
def save_game(gameId, playerId):
    slotId = request.args.get("slotId", "default")

    player_progress = request.json
    if not player_progress:
        return jsonify({"error": "Not found"}), 400

    #store in dictionary
    saves[(gameId, playerId, slotId)] = player_progress

    return jsonify({"message": f"Save stored in slot '{slotId}'"}), 201


# ---------Load------------
@app.route("/games/<gameId>/players/<playerId>/save", methods=["GET"])
def load_game(gameId, playerId):
    # default if no slot provided
    slotId = request.args.get("slotId", "default")

    player_progress = saves.get((gameId, playerId, slotId))
    if player_progress is None:
        return jsonify({"error": f"No save found"}), 404

    return jsonify(player_progress), 200


if __name__ == "__main__":
    app.run(debug=True)