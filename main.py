import arcade

SCREEN_HEIGHT   = 600
SCREEN_WIDTH    = 800
UPDATE_RATE     = 1./60

class Player(arcade.Sprite):
    def __init__(self, x, y, filename='assets/tank.png', scale=0.5):
        super().__init__(filename, center_x=x, center_y=y)

        self.velocity = [0, -1];

# Game class:
class GoldDigger(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BEIGE)
        self.set_update_rate(UPDATE_RATE)
        self.sprite_list = arcade.SpriteList()

        self.tank = Player(x=400, y=300, scale=0.4)

        self.sprite_list.append(self.tank)

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