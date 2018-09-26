from gameObject.staticGameObject import StaticGameObject


class Drill(StaticGameObject):
    def __init__(self, local_x=0, local_y=0, drill_rate=1.0, level=0):
        super().__init__('assets/tank__'+str(level)+'/drill.png', x, y)

        self.drill_rate = drill_rate
        self.level = level                      # compare to drilled mineral level

    def tick(self, dt):
        pass

    def level_up(self):
        self.level += 1;
        self.update_sprite(newPath='assets/tank__'+str(self.level)+'drill.png')
        self.drill_rate *= 2.0