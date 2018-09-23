import random
from gameObject.environment.blocks.block import Block


class BlockFactory:
    def __init__(self, start_x, start_y, unit):
        self.start_x = start_x
        self.start_y = start_y
        self.unit = unit

    def generate_ground(self, start_x, start_y, unit):
        bf = BlockFactory(start_x, start_y, unit)
        blocks = []
        for i in range(-15, 15):
            for j in range(4):
                block = bf.get_block(i, j)
                if block is not None:
                    blocks.append(block)
        return blocks

    def get_block(self, x, y):
        block_map = [
            dict(
                url="empty",
                value=0,
                density=100
            ),
            dict(
                url="assets/tiles/ground_tile.png",
                value=0,
                density=10
            ),
            dict(
                url="assets/tiles/ground_tile.png",
                value=0,
                density=10
            ),
            dict(
                url="assets/tiles/gold_tile.png",
                value=100,
                density=100
            ),
            dict(
                url="assets/tiles/silver_tile.png",
                value=100,
                density=100
            ),
        ]
        randint = random.randint(0,25)
        block_type = 0

        if randint < 2:
            block_type = 0
        elif randint < 17:
            block_type = 1
        elif randint < 20:
            block_type = 2
        elif randint < 23:
            block_type = 3
        else:
            block_type = 4

        chosen = block_map[block_type]
        if block_type != 0:
            return Block(self.start_x + x*self.unit+1 ,self.start_y + y*self.unit+1, chosen["url"], chosen["value"], chosen["density"], None)
        else:
            return None
