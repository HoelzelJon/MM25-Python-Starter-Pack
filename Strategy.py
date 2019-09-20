from API import Game


class Strategy(Game):
    """
        FILL THIS METHOD OUT FOR YOUR BOT:
        Method to set unit initializations. Run at the beginning of a game, after assigning player numbers.
        We have given you a default implementation for this method.
        OUTPUT:
            An array of 3 dictionaries, where each dictionary details a unit. The dictionaries should have the following fields
                "health": An integer indicating the desired health for that unit
                "speed": An integer indicating the desired speed for that unit
                "unitId": An integer indicating the desired id for that unit. In this provided example, we assign Ids 1,2,3 if you are player1, or 4,5,6 if you are player2
                "attackPattern": a 7x7 2d integer list indicating the desired attack pattern for that unit
                "terrainPattern": a 7x7 2d boolean list indicating the desired terrain pattern for that unit.
        Note: terrainPattern and attackPattern should be indexed x,y. with (0,0) being the bottom left
        If player_id is 1, UnitIds for the bots should be 1,2,3. If player_id is 2, UnitIds should be 4,5,6
    """
    def get_setup(self):
        units = []
        for i in range(3):
            unit = {"health": 5, "speed": 5}
            unit["attackPattern"] = [[0] * 7 for j in range(7)]
            # if you are player1, unitIds will be 1,2,3. If you are player2, they will be 4,5,6
            unit["unitId"] = i + 1
            if self.player_id == 2:
                unit["unitId"] += 3
            unit["terrainPattern"] = [[False]*7 for j in range(7)]
            # These sample bot will do damage to the tiles to its left, right, and up. And build terrain behind it
            unit["attackPattern"][3][2] = 2
            unit["attackPattern"][3][4] = 2
            unit["attackPattern"][2][3] = 2
            unit["attackPattern"][4][2] = 2
            unit["terrainPattern"][3][2] = True
            units.append(unit)
        return units

    """
        FILL THIS METHOD OUT FOR YOUR BOT:
        Method to implement the competitors strategy in the next turn of the game.
        We have given you a default implementation here.
        OUTPUT:
            A list of 3 dictionaries, each of which indicates what to do on a given turn with that specific unit. Each dictionary should have the following keys:
                "unitId": The Id of the unit this dictionary will detail the action for
                "movement": an array of directions ("UP", "DOWN", "LEFT", or "RIGHT") details how you want that unit to move on this turn
                "attack": the direction in which to attack ("UP", "DOWN", "LEFT", or "RIGHT")
                "priority": The bots move one at a time, so give the priority which you want them to act in (1,2, or 3)
    """
    def do_turn(self):
        my_units = self.get_my_units()
        decision = [{
            "priority": i+1,
            "movement": ["DOWN"]*my_units[i].speed,
            "attack": "DOWN",
            "unitId": my_units[i].id
            } for i in range(len(my_units))]
        return decision
