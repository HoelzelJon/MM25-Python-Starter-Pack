from API import Game


class Strategy(Game):
    def get_setup(self):
        return [{
            "attackPattern": [[0] * 7 for j in range(7)],
            "health": 5,
            "speed": 4
        } for i in range(3)]

    def do_turn(self):
        decision = {}
        priorities = [1, 2, 3]
        decision['priorities'] = priorities
        decision['movements'] = [['DOWN', 'DOWN', 'DOWN', 'DOWN']
                                 for i in range(3)]
        decision['attacks'] = ['UP', 'LEFT', 'RIGHT']
        return decision
