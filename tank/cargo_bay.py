from gameObject.staticGameObject import StaticGameObject

class CargoBay(StaticGameObject):

    def __init__(self, local_x=0, local_y=0, capacity=100., level=0):
        super().__init__('assets/tank__'+str(level)+'/cargo_bay.png', local_x, local_y, )

        self.capacity = capacity        # kg
        self.cargo = []                 # list of all minerals contained
        self.cargo_mass = 0             # kg
        self.status = 0                 # percentage

        self.level = level

    def tick(self, dt):
        pass

    def collect_cargo(self, mineral_o):
        if self.cargo_mass + mineral_o.mass <= self.capacity:
            self.cargo.append(mineral_o)
            self.cargo_mass += mineral_o.mass
            self.status = int(100 * self.cargo_mass / self.capacity)
        else:
            print('CARGO FULL!')

    def level_up(self):
        self.update_sprite(newPath='assets/tank__'+str(self.level)+'cargo_bay.png')
        self.capacity *= 2.0