# 万：1-9
# 饼：21-29
# 条：41-49
# 东：60
# 西：70
# 南：80
# 北：90
# 中: 100
# 发：110
# 白：120

class Tile:
    def __init__(self, type, num=0):
        self.type = type
        self.id = 0
        self.num = num

        if type == "wan":
            self.id = num
        elif type == "bing":
            self.id = 20 + num
        elif type == "tiao":
            self.id = 40 + num
        elif type == "dongfeng":
            self.id = 60
        elif type == "xifeng":
            self.id = 70
        elif type == "nanfeng":
            self.id = 80
        elif type == "beifeng":
            self.id = 90
        elif type == "zhong":
            self.id = 100
        elif type == "fa":
            self.id = 110
        elif type == "bai":
            self.id = 120
        else:
            print("invalid type")


    def __lt__(self, other):
        return self.id < other.id


    def __eq__(self, other):
        return self.id == other.id


    def __gt__(self, other):
        return self.id > other.id


    def __hash__(self):
        return hash(self.id)


    def next(self):
        return Tile(self.type, self.num+1)


class TileFactory:
    def __init__(self):
        self.checked = []
        self.tiles = []


    def add(self, tile):
        self.tiles.append(tile)


    def print(self, lst):
        for i in lst:
            print("tile id, type, num: ", i.id, i.type, i.num)


    def check(self):
        if len(self.tiles) != 14:
            print('Fried Hu. Number of tiles is wrong')
            return False

        self.tiles.sort()

        pairs = set()
        for i in range(1, len(self.tiles)):
            if self.tiles[i-1] == self.tiles[i]:
                pairs.add(self.tiles[i])

        if len(pairs) == 0:
            print("Fried Hu. No pairs.")
            return False

        for pair in pairs:
            remain = self.tiles.copy()
            remain.remove(pair)
            remain.remove(pair)
            if self.huPai(remain):
                print("-------------------------------------------------------")
                print("jiang:")
                self.print([pair])
                print("-------------------------------------------------------")
                print("others:")
                self.print(remain)
                print("-------------------------------------------------------")
                return True

        return False


    def huPai(self, lst):
        if len(lst) == 0:
            return True

        if lst[0] == lst[1] and lst[1] == lst[2]:
            return self.huPai(lst[3:])
        else:
            curTile = lst[0]
            nextTile = curTile.next()
            nextNextTile = nextTile.next()
            if nextTile in lst and nextNextTile in lst:
                lst.remove(curTile)
                lst.remove(nextTile)
                lst.remove(nextNextTile)
                return self.huPai(lst)

        return False



tileFactory = TileFactory()

# tile_list = [ Tile("wan", 3), Tile("wan", 1), Tile("wan", 2),
#               Tile("tiao", 3), Tile("tiao", 3), Tile("tiao", 3),
#               Tile("tiao", 3), Tile("tiao", 4), Tile("tiao", 5),
#               Tile("tiao", 6), Tile("tiao", 7), Tile("tiao", 8),
#               Tile("zhong"), Tile("zhong")
#             ]

tile_list = [ Tile("tiao", 3), Tile("tiao", 1), Tile("tiao", 2),
              Tile("tiao", 1), Tile("tiao", 1), Tile("tiao", 1),
              Tile("tiao", 2), Tile("tiao", 3), Tile("tiao", 4),
              Tile("tiao", 6), Tile("tiao", 7), Tile("tiao", 8),
              Tile("zhong"), Tile("zhong")
            ]


for tile in tile_list:
    tileFactory.add(tile)

print("input tiles: ")
tileFactory.print(tile_list)


result = tileFactory.check()
print("hu pai?: ", result)

