from queue import Queue
import copy
# class for Position Object
class Position:
    # A position will have an x and y coordinate
    def __init__(self, position_json):
        self.x = position_json["x"]
        self.y = position_json["y"]

# Class for a Unit Object
class Unit:
    # A unit will have the following fields
    def __init__(self, unit_json):
        self.hp = unit_json["hp"]
        self.speed = unit_json["speed"]
        self.attack = unit_json["attack"]
        self.terrain = unit_json["terrain"]
        self.id = unit_json["id"]
        self.player_id = unit_json["playerNum"]
        self.pos = Position(unit_json["pos"])

# Class for a Tile Object
class Tile:
    # A Tile will have an id, hp, and type where type is either 'BLANK', 'DESTRUCTIBLE', or 'INDESTRUCTIBLe'
    def __init__(self, tile_json):
        self.id = tile_json["id"]
        self.hp = tile_json["hp"]
        self.type = tile_json["type"]

# Class for a Game Object
class Game:
    # A Game Object will have a player_id, game_id, and the game represented as a json
    def __init__(self, game_json):
        self.game = game_json
        self.player_id = self.game['playerNum']
        self.game_id = self.game["gameId"]
    def get_setup(self):
        raise NotImplementedError(
            "Please Implement this method in a \"Strategy\" class")

    def do_turn(self):
        raise NotImplementedError(
            "Please Implement this method in a \"Strategy\" class")

	# Implement this in the "Strategy" class if you want to do something specific
	# when a game ends
    def game_over(self, result):
        pass

    # updates the game json. Called every turn
    def update_game(self, game_json):
        self.game = game_json

    """
        Given a player_id, returns the units for that team.
        INPUT:
            player_id: The id of the player to get units for
        OUTPUT:
            A list of Unit objects corresponding to that player_id
    """
    def get_units_for_team(self, player_id):
        units = []
        for unit in self.game["units"]:
            if unit["playerNum"] == player_id:
                units.append(Unit(unit))
        return units

    """
        Gets my units
        OUTPUT:
            A list of Unit Objects corresponding to my units
    """
    def get_my_units(self):
        return self.get_units_for_team(self.player_id)

    """
        Gets the units for the enemy player
        OUTPUT:
            A list of Unit Objects corresponding to the enemy's units
    """
    def get_enemy_units(self):
        if self.player_id == 1:
            return self.get_units_for_team(2)
        else:
            return self.get_units_for_team(1)

    """
        Returns the Tile at a given x and y
        INPUT:
            position: a tuple (x,y) specifying the desired x and y coordinates
        OUTPUT:
            The Tile Object corresponding to that position
    """
    def get_tile(self, position):
        tile_json =  self.game["tiles"][position[0]][position[1]]
        return Tile(tile_json)

    """
        Returns the unit at a given position
        INPUT:
            position: a tuple (x,y) specifying the desired x and y coordinates
        OUTPUT:
            If there is a unit at that position, the Unit object at that position
            If no unit is at that position, return None
    """
    def get_unit_at(self, position):
        unit_at_pos = None
        for unit in self.game["units"]:
            if unit["pos"]["x"] == position[0] and unit["pos"]["y"] == position[1]:
                unit_at_pos = Unit(unit)
                break
        return unit_at_pos

    """
        Get the shortest valid path from start to end position while avoiding tiles in tiles_to_avoid
        INPUT:
            start_position: a tuple (x,y) specifying the x and y coordinate of the start_position
            end_position: a tuple (x,y) specifying the x and y coordinates of the end position
            tiles_to_avoid: a list of tuples (x,y) specifying the x and y coordinates of tiles to avoid
        OUTPUT:
            A list of directions ('UP', 'DOWN', 'LEFT', or 'RIGHT') specifying how to get from the start_position to the end_position while avoiding the specified tiles
            If no path exists, returns an None
    """
    # Start and end position are tuples (x,y). tiles_to_avoid is a list of such tuples
    def path_to(self, start_position, end_position, tiles_to_avoid=[]):
        q = Queue()
        q.put((start_position, []))
        visited = [[False for i in range(len(self.game["tiles"]))] for j in range(len(self.game["tiles"]))]
        while not q.empty():
            position, directions = q.get()
            if visited[position[1]][position[0]]:
                continue
            else:
                visited[position[1]][position[0]] = True
            if position == end_position:
                return directions
            left = (position[0] - 1, position[1])
            if not ((left[0] < 0) or (left in tiles_to_avoid) or (self.get_tile(left).type != "BLANK")):
                left_directions = copy.copy(directions)
                left_directions.append("LEFT")
                q.put((left, left_directions))
            right = (position[0] + 1, position[1])
            if not ((right[0] >= len(self.game["tiles"])) or (right in tiles_to_avoid) or (self.get_tile(right).type != "BLANK")):
                right_directions = copy.copy(directions)
                right_directions.append("RIGHT")
                q.put((right, right_directions))
            down = (position[0], position[1] + 1)
            if not ((down[1] >= len(self.game["tiles"][0])) or (down in tiles_to_avoid) or (self.get_tile(down).type != "BLANK")):
                down_directions = copy.copy(directions)
                down_directions.append("DOWN")
                q.put((down, down_directions))
            up = (position[0], position[1] - 1)
            if not ((up[1] < 0) or (up in tiles_to_avoid) or (self.get_tile(up).type != "BLANK")):
                up_directions = copy.copy(directions)
                up_directions.append("UP")
                q.put((up, up_directions))
        return None

    # gets the unit with a given id
    def get_unit(self, unit_id):
        for unit in self.get_my_units():
            if unit.id == unit_id:
                return unit
        for unit in self.get_enemy_units():
            if unit.id == unit_id:
                return unit
        return None

    """
      Given a unit_id and direction, returns where an attack in a certain direction would land on the map
      Optionally provide a position to use instead of the units current position. position should be tuple of the location (x,y)
      Returns a list of tuples of the form (pos, attack_damage) where pos is a Position Object
    """
    def get_positions_of_attack_pattern(self, unit_id, direction, position = None):
        unit = self.get_unit(unit_id)
        attack_pattern = unit.attack
        if direction == 'RIGHT':
            attack_pattern = self.rotate_attack_pattern(attack_pattern)
        elif direction == 'DOWN':
            attack_pattern = self.rotate_attack_pattern(attack_pattern)
            attack_pattern = self.rotate_attack_pattern(attack_pattern)
        elif direction == 'LEFT':
            attack_pattern = self.rotate_attack_pattern(attack_pattern)
            attack_pattern = self.rotate_attack_pattern(attack_pattern)
            attack_pattern = self.rotate_attack_pattern(attack_pattern)
        elif direction != 'UP':
            return None
        attacks = []
        for row in range(len(attack_pattern)):
            for col in range(len(attack_pattern[row])):
                attack = attack_pattern[row][col]
                if attack == 0:
                    continue
                # assume that unit is at the center of the 7 by 7 attack pattern
                x_pos = unit.pos.x
                y_pos = unit.pos.y
                if position:
                    x_pos = position[0]
                    y_pos = position[1]
                x_coordinate = x_pos + col - 3
                y_coordinate = y_pos + row - 3
                if x_coordinate >= 0 and x_coordinate < len(self.game["tiles"]) and y_coordinate >= 0 and y_coordinate < len(self.game["tiles"][0]):
                    attacks.append((Position({"x": x_coordinate, "y": y_coordinate}), attack))
        return attacks

    def rotate_attack_pattern(self, attack):
        list_of_tuples = zip(*attack[::-1])
        return [list(elem) for elem in list_of_tuples]
