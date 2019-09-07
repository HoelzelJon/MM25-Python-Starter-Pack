from queue import Queue


class Position:
    def __init__(self, position_json):
        self.x = position_json['x']
        self.y = position_json['y']


class Unit:
    def __init__(self, unit_json):
        self.hp = unit_json['hp']
        self.speed = unit_json['speed']
        self.attack = unit_json['attack']
        self.isAlive = unit_json['isAlive']
        self.id = unit_json['id']
        self.pos = Position(unit_json['pos'])


class Tile:
    def __init__(self, tile_json):
        self.id = tile_json['id']
        self.hp = tile_json['hp']
        self.unit = tile_json.get('unit', None)
        self.type = tile_json['type']


class Game:
    # pass in player Id as 1 or 2
    def __init__(self, game_json, player_id):
        self.game = game_json
        self.player_id = player_id
        self.game_id = self.game['gameId']

    def get_setup(self):
        raise NotImplementedError(
            "Please Implement this method in a \"Strategy\" class")

    def do_turn(self):
        raise NotImplementedError(
            "Please Implement this method in a \"Strategy\" class")

    # updates the game json. Called every turn
    def update_game(self, game_json):
        self.game = game_json

    def convert_json_to_units(UnitsJson):
        units = []
        for unitJson in UnitsJson:
            units.append(Unit(unitJson))
        return units

    # Returns the player's units
    def get_my_units(self):
        if self.playerId == 1:
            return self.convert_json_to_units(self.game['p1Units'])
        else:
            return self.convert_json_to_units(self.game['p2Units'])

    # Returns the opponents units
    def get_enemy_units(self):
        if self.playerId == 1:
            return self.convert_json_to_units(self.game['p2Units'])
        else:
            return self.convert_json_to_units(self.game['p1Units'])

    # Return the tile object at a give x and y. Takes a position tuple (x,y)
    def get_tile(self, position):
        tile_json = self.game['map']['tiles'][position[0]][position[1]]
        return Tile(tile_json)

    # Returns the unit at the given position, if there is one. Takes a position
    # tuple (x,y)  v
    def get_unit_at(self, position):
        tile = self.get_tile(position[0], position[1])
        return tile.unit

    # Get the shortest valid path from start to end position while avoiding
    # tiles in tilesToAvoid
    # Start and end position are tuples (x,y)
    def path_to(self, start_position, end_position, tiles_to_avoid=[]):
        q = Queue()
        q.put((start_position, []))
        # 12 x 12 is the dimension of the board
        visited = [[False for i in range(12)] for j in range(12)]
        while len(q) > 0:
            position, directions = q.get()
            if visited[position[1]][position[0]]:
                continue
            else:
                visited[position[1]][position[0]] = True
            if position == end_position:
                return directions
            left = (position[0] - 1, position[1])
            if not ((left[0] < 0) or (left in tiles_to_avoid) or
                    (self.getTile(left).type != 'BLANK')):
                left_directions = directions.copy()
                left_directions.append('LEFT')
                q.put((left, left_directions))
            right = (position[0] + 1, position[1])
            if not ((right[0] >= len(self.game['map']['tiles'][0])) or
                    (right in tiles_to_avoid) or
                    (self.get_tile(right).type != 'BLANK')):
                right_directions = directions.copy()
                right_directions.append('RIGHT')
                q.put((right, right_directions))
            down = (position[0], position[1] - 1)
            if not ((down[1] < 0) or (down in tiles_to_avoid) or
                    (self.get_tile(down).type != 'BLANK')):
                down_directions = directions.copy()
                down_directions.append('DOWN')
                q.put((down, down_directions))
            up = (position[0], position[1] + 1)
            if not ((up[1] >= len(self.game['map']['tiles'])) or
                    (up in tiles_to_avoid) or
                    (self.get_tile(up).type != 'BLANK')):
                up_directions = directions.copy()
                up_directions.append('UP')
                q.put((up, up_directions))
        return None
