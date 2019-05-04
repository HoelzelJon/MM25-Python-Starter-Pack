from flask import Flask, request
import json
import sys

games = {}
app = Flask(__name__)

class Game:
	#declare any variables here

	def do_turn(self, game_state):
		#perform the actions for a term
		decision = {}
		priorities = [1,2,3]
		decision['priorities'] = priorities
		decision['movements'] = [['DOWN', 'DOWN', 'DOWN', 'DOWN'] for i in range(3)]
		decision['attacks'] = ['UP', 'LEFT', 'RIGHT']
		return decision

@app.route('/game_init', methods = ['POST'])
def game_init():
	#specify the attack patterns for each player
	# Return a 3d array. there will be 3 layers (1 for each bot) each layer will be a 2d array of the attack pattern of the bot
	
	state = request.get_json(force=True)
	
	games[state.get('gameId', 'game1')] = Game()

	setup = [{"attackPattern": [[0]*7 for j in range(7)],
			  "health": 5, "speed": 4} for i in range(3)]
	
	return json.dumps(setup)

@app.route('/turn', methods = ['POST'])
def turn():
	game_state = request.get_json(force=True)
	my_game = games[game_state.get('gameId', 'game1')]
	decision = my_game.do_turn(game_state)
	return json.dumps(decision)

@app.route('/game_over', methods = ['POST'])
def game_over():
	end_state = request.get_json(force=True)
	games.pop(end_state.get('gameId', 'game'), None)
	return json.dumps(end_state)

if __name__ == "__main__":
    app.run(port=int(sys.argv[1]))
