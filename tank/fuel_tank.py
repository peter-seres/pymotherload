from gameObject.staticGameObject import StaticGameObject


class FuelTank(StaticGameObject):
    def __init__(self, parent_tank, local_x=0, local_y=0, capacity=10., level=0):
        super().__init__('assets/tank__'+str(level)+'/fuel_tank.png', local_x, local_y)
        self.capacity = capacity
        self.fuel_left = capacity

        self.threshold = 20
        self.threshold_crit = 10

        self.tank = parent_tank
        self.fuel_level = 100

        self.fuel_warning = False
        self.level = 0

    def tick(self, dt):
        self.fuel_left -= self.tank.engine.consumption * dt
        self.fuel_level = int(100*self.fuel_left/self.capacity)

        if self.threshold_crit <= self.fuel_level <=  self.threshold:
            self.send_warning()
        elif 0 <= self.fuel_level <=  self.threshold_crit:
            self.send_warning()

        elif self.fuel_level <= 0:
            self.fuel_level = 0
            self.fuel_left = 0
            self.send_warning()
        else:
             self.fuel_warning = False

        self.tank.engine.consumption = self.tank.engine.idle_consumption

    def fill_up(self):
        self.fuel_left = self.capacity

    def send_warning(self):
        self.fuel_warning = True

    def level_up(self):
        self.level += 1;
        self.update_sprite(newPath='assets/tank__'+str(self.level)+'fuel_tank.png')
        self.capacity *= 1.2

