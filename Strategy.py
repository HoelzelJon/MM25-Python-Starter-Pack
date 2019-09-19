from API import Game


class Strategy(Game):
    def get_setup(self):
        units = []
        for i in range(3):
            unit = {"health": 5, "speed": 4}
            unit["attackPattern"] = [[0] * 7 for j in range(7)]
            # if you are player1, unitIds will be 1,2,3. If you are player2, they will be 4,5,6
            unit["unitId"] = i + 1
            if self.player_id == 2:
                unit["unitId"] += 3
            unit["terrainPattern"] = [[False]*7 for j in range(7)]
            units.append(unit)
        return units

    def do_turn(self):
        my_units = self.get_my_units()

        decision = [{
            "priority": i+1,
            "movement": ["DOWN"]*my_units[i].speed,
            "attack": "DOWN",
            "unitId": my_units[i].id
            } for i in range(len(my_units))]
        return decision
