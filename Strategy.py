from API import Game


class Strategy(Game):
    def get_setup(self):
        units = []
        for i in range(3):
            unit = {"health": 5, "speed": 4}
            unit["attackPattern"] = [[0] * 7 for j in range(7)]
            unit["unitId"] = i + 1
            unit["terrainPattern"] = [[False]*7 for j in range(7)]
            units.append(unit)
        return units

    def do_turn(self):
        decision = {}
        priorities = [1, 2, 3]
        decision['priorities'] = priorities
        decision['movements'] = [['DOWN', 'DOWN', 'DOWN', 'DOWN']
                                 for i in range(3)]
        decision['attacks'] = ['UP', 'LEFT', 'RIGHT']
        return decision
