from queue import Queue
import copy
class Position:
    def __init__(self, position_json):
        self.x = position_json["x"]
        self.y = position_json["y"]


class Unit:
    def __init__(self, unit_json):
        self.hp = unit_json["hp"]
        self.speed = unit_json["speed"]
        self.attack = unit_json["attack"]
        self.isAlive = unit_json["isAlive"]
        self.id = unit_json["id"]
        self.pos = Position(unit_json["pos"])


class Tile:
    def __init__(self, tile_json):
        self.id = tile_json["id"]
        self.hp = tile_json["hp"]
        self.unit = tile_json.get("Unit", None)
        self.type = tile_json["type"]


class Game:
    # pass in player Id as 1 or 2
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

    # updates the game json. Called every turn
    def update_game(self, game_json):
        self.game = game_json

    def convert_json_to_units(self, units_json):
        units = []
        for unit_json in units_json:
            units.append(Unit(unit_json))
        return units

    # Returns the player"s units
    def get_my_units(self):
        if self.player_id == 1:
            return self.convert_json_to_units(self.game["p1Units"])
        else:
            return self.convert_json_to_units(self.game["p2Units"])

    # Returns the opponents units
    def get_enemy_units(self):
        if self.player_id == 1:
            return self.convert_json_to_units(self.game["p2Units"])
        else:
            return self.convert_json_to_units(self.game["p1Units"])

    # Return the tile object at a give x and y. Takes a position tuple (x,y)
    def get_tile(self, position):
        tile_json =  self.game["map"]["tiles"][position[1]][position[0]]
        return Tile(tile_json)

    # Returns the unit at the given position, if there is one. Takes a position
    # tuple (x,y)  v
    def get_unit_at(self, position):
        tile = self.get_tile((position[0], position[1]))
        for unit in self.get_my_units():
            if unit.id == tile.unit:
                return unit
        for unit in self.get_enemy_units():
            if unit.id == tile.unit:
                return unit
        return None
    # Get the shortest valid path from start to end position while avoiding tiles in tiles_to_avoid
    # Start and end position are tuples (x,y). tiles_to_avoid is a list of such tuples
    def path_to(self, start_position, end_position, tiles_to_avoid=[]):
        q = Queue()
        q.put((start_position, []))
        visited = [[False for i in range(len(self.game["map"]["tiles"]))] for j in range(len(self.game["map"]["tiles"]))]
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
            if not ((right[0] >= len(self.game["map"]["tiles"][0])) or (right in tiles_to_avoid) or (self.get_tile(right).type != "BLANK")):
                right_directions = copy.copy(directions)
                right_directions.append("RIGHT")
                q.put((right, right_directions))
            down = (position[0], position[1] + 1)
            if not ((down[1] >= len(self.game["map"]["tiles"])) or (down in tiles_to_avoid) or (self.get_tile(down).type != "BLANK")):
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
      Returns a list of tuples of the form (attack_damage, pos) where pos is a Position Object
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
                if x_coordinate >= 0 and x_coordinate < len(self.game["map"]["tiles"][0]) and y_coordinate >= 0 and y_coordinate < len(self.game["map"]["tiles"]):
                    attacks.append((attack, Position({"x": x_coordinate, "y": y_coordinate})))
        return attacks

    def rotate_attack_pattern(self, attack):
        list_of_tuples = zip(*attack[::-1])
        return [list(elem) for elem in list_of_tuples]
