from flask import Flask, request
import json
import sys
from importlib import import_module

games = {}
app = Flask(__name__)


@app.route('/game_init', methods=['POST'])
def game_init():
    state = request.get_json(force=True)

    my_game = Strategy(state, state['playerNum'])
    games[state.get('gameId', 'game1')] = my_game

    setup = my_game.get_setup()

    return json.dumps(setup)


@app.route('/turn', methods=['POST'])
def turn():
    game_state = request.get_json(force=True)
    my_game = games[game_state.get('gameId', 'game1')]
    my_game.update_game(game_state)
    decision = my_game.do_turn()
    return json.dumps(decision)


@app.route('/game_over', methods=['POST'])
def game_over():
    end_state = request.get_json(force=True)
    games.pop(end_state.get('gameId', 'game'), None)
    return json.dumps(end_state)


if __name__ == "__main__":
    module = import_module(sys.argv[1])  # import the player strategy file
    Strategy = getattr(module, 'Strategy')
    app.run(port=int(sys.argv[2]), debug=True)
