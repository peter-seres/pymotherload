import arcade
import random

# Global constants
SCREEN_HEIGHT   = 600
SCREEN_WIDTH    = 800
UPDATE_RATE     = 1./60
GRAVITY         = 0.1


# Terrain / ground tile class. Things to be mined:
class Block(arcade.Sprite):
    def __init__(self, x, y, filename='assets/tiles/ground_tile.png', scale=1.0, value=0):
        super().__init__(filename, center_x=x, center_y=y, scale=scale)

        self.value = value
        self.being_drilled = False

    def set_being_drilled(self, bool):
        pass

    def check_render_distance(self):
        pass

    def view_offset(self):
        pass

# Player class. Make it a modular tank that can have upgraded engine/cargo/cooler etc.
class Player(arcade.Sprite):
    def __init__(self, x, y, filename='assets/tank_simple2_512.png', scale=0.1):
        super().__init__(filename, center_x=x, center_y=y, scale=scale)
        self.hor_speed = 2
        self.engine_on = False
        self.acceleration = 4

    def lose_hp(self):
        pass

    def repair(self):
        pass

    def lose_fuel(self):
        pass

    def refuel(self):
        pass

    def add_cargo(self):
        pass

    def sell_cargo(self):
        pass

    def drill_down(self):
        pass

    def drill_left(self):
        pass

    def drill_right(self):
        pass

    def physics(self):
        self.change_y -= GRAVITY

        if self.engine_on:
            self.change_y += self.acceleration * GRAVITY

    def set_fly(self, bool):
        self.engine_on = bool

# Game class:
class GoldDigger(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BEIGE)
        self.set_update_rate(UPDATE_RATE)
        self.static_sprite_list = arcade.SpriteList()
        self.dynamic_sprite_list = arcade.SpriteList()

        # Create terrain:
        tile_scale = 0.1
        self.generate_terrain(20, 20, tile_scale)

        # Create player object:
        self.tank = Player(x=400, y=300, scale=tile_scale)
        self.dynamic_sprite_list.append(self.tank)

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
                    self.static_sprite_list.append(block)

    def on_mouse_press(self, x, y, button, modifiers):
        if button==arcade.MOUSE_BUTTON_LEFT:
            self.tank.set_fly(True)

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Release the item we are holding (if any)
            self.tank.set_fly(False)

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            self.tank.set_fly(True)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.tank.change_x = -self.tank.hor_speed
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.tank.change_x = self.tank.hor_speed

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP or key == arcade.key.W:
            self.tank.set_fly(False)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.tank.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.tank.change_x = 0

    def on_draw(self):
        arcade.start_render()

        # Render all sprites in sprite_list:
        self.static_sprite_list.draw()
        self.dynamic_sprite_list.draw()

        # Test screem text:
        # text = f"Screen text: {88.8:.1f}"
        arcade.draw_text('Movement: W, A, D or UP, LEFT, RIGHT', 20, SCREEN_HEIGHT - 20, arcade.color.BLACK_BEAN, 12)

    def update(self, delta_time: float):
        self.tank.physics()
        self.dynamic_sprite_list.update()

def main():
    GoldDigger(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()