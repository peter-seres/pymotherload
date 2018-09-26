import arcade
import random

SCREEN_HEIGHT   = 600
SCREEN_WIDTH    = 800
UPDATE_RATE     = 1./60

class Block(arcade.Sprite):
    def __init__(self, x, y, filename='assets/tiles/ground_tile.png', scale=1.0, value=0):
        super().__init__(filename, center_x=x, center_y=y, scale=scale)

        self.value = value
        self.being_drilled = False

class Player(arcade.Sprite):
    def __init__(self, x, y, filename='assets/tank.png', scale=0.05):
        super().__init__(filename, center_x=x, center_y=y, scale=scale)

        self.velocity = [0, -1]

# Game class:
class GoldDigger(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BEIGE)
        self.set_update_rate(UPDATE_RATE)
        self.sprite_list = arcade.SpriteList()

        # Create terrain:
        tile_scale = 0.1
        self.generate_terrain(20, 20, tile_scale)

        # Create player object:
        self.tank = Player(x=400, y=300, scale=tile_scale*2)
        self.sprite_list.append(self.tank)

    # Generate a number of blocks to serve as ground/terrain:
    def generate_terrain(self, N_hor, N_vert, tile_scale):
        start_x = 0
        start_y = SCREEN_HEIGHT/2
        size = 512 * tile_scale

        tile_files = ['assets/tiles/ground_tile.png', 'assets/tiles/gold_tile.png', 'assets/tiles/silver_tile.png']

        for i in range(N_hor):
            for j in range(N_vert):
                randint = random.randint(0, 100)

                if randint < 10:
                    block_type = 0
                elif randint < 70:
                    block_type = 1
                elif randint < 90:
                    block_type = 2
                else:
                    block_type = 3

                chosen_file = tile_files[block_type-1]
                if block_type != 0:
                    block = Block(x=start_x+i*size+1, y=start_y-j*size+1, filename=chosen_file, scale=tile_scale)
                    self.sprite_list.append(block)

    def on_mouse_press(self, x, y, button, modifiers):
        if button==arcade.MOUSE_BUTTON_LEFT:
            self.tank.velocity = [0, 10]

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Release the item we are holding (if any)
            self.tank.velocity = [0, -1]

    def on_draw(self):
        arcade.start_render()

        # Render all sprites in sprite_list:
        self.sprite_list.draw()

        # Test screem text:
        text = f"Screen text: {88.8:.1f}"
        arcade.draw_text(text, 20, SCREEN_HEIGHT - 20, arcade.color.BLACK_BEAN, 12)

    def update(self, delta_time: float):
        self.sprite_list.update()
        pass

def main():
    GoldDigger(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()