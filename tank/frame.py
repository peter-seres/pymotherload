from gameObject.staticGameObject import StaticGameObject


class Frame(StaticGameObject):
    def __init__(self, local_x = 0, local_y=0, hp=100, level=0):
        super().__init__('assets/tank__'+str(level)+'/frame.png', local_x, local_y)
        self.hp = hp                            # percentage
        self.velocity_threshold = 200.
        self.rate_of_injury = 10.               # percentage

        self.level = level

    def lose_health(self):
        self.hp -= self.rate_of_injury

    def flash_red(self):
        pass

    def refresh_collider(self):
        self.rect.center = (self.x, self.y)

    def tick(self, dt):
        pass

    def level_up(self):
        self.level += 1;
        self.update_sprite(newPath='assets/tank__'+str(self.level)+'frame.png')
        self.rate_of_injury *= 0.6

    def repair(self):
        self.hp = 100
