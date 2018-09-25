import arcade

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Player:
    def __init__(self, x, y, filename='assets/tank.png', scale=0.5):

        self.sprite = arcade.Sprite(filename=filename, scale=scale)
        self.sprite.center_x = x
        self.sprite.center_y = y


# Game class:
class GoldDigger(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BEIGE)

        self.sprite_list = arcade.SpriteList()

        tank = Player(x=400, y=300, scale=0.4)

        self.sprite_list.append(tank.sprite)

    def on_draw(self):
        arcade.start_render()

        # Render all sprites in sprite_list:
        self.sprite_list.draw()

        # Test screem text:
        text = f"Screen text: {88.8:.1f}"
        arcade.draw_text(text, 20, SCREEN_HEIGHT - 20, arcade.color.BLACK_BEAN, 12)

    def update(self, delta_time: float):
        pass

def main():
    GoldDigger(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()