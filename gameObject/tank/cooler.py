from gameObject.staticGameObject import StaticGameObject

class Cooler(StaticGameObject):

    def __init__(self, local_x=0, local_y=0, cooling_rate=1., level=0):
        super().__init__('assets/tank__'+str(level)+'/cooler.png', local_x, local_y)

        self.cooling_rate = cooling_rate
        self.level = level

    def tick(self, dt):
        pass

    def level_up(self):
        self.level += 1;
        self.update_sprite(newPath='assets/tank__'+str(self.level)+'cooler.png')
        self.cooling_rate *= 2.0