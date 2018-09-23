from gameObject.staticGameObject  import GLOBAL_OFFSET
from gameObject.dynamicGameObject import DynamicGameObject
from gameObject.tank.cargo_bay import CargoBay
from gameObject.tank.cooler import Cooler
from gameObject.tank.engine import Engine
from gameObject.tank.fuel_tank import FuelTank
from gameObject.tank.frame import Frame
from gameObject.tank.drill import Drill
from game_mode_constants import *


class Tank(DynamicGameObject):
    def __init__(self, x, y, m):
        self.frame      = Frame(hp=100, level=1)
        self.engine     = Engine(lift=250000., side_force=250000., level=1)
        self.cooler     = Cooler(cooling_rate=10., level=1)
        self.fuel_tank  = FuelTank(self, capacity=30., level=1)
        self.cargo_bay  = CargoBay(capacity=100., level=1)
        #self.drill      = Drill(100, 0, 12.)

        self.components = [self.frame,
                           self.engine,
                           self.cooler,
                           self.fuel_tank,
                           self.cargo_bay,]

        self.ground = None
        self.landed = False
        self.__x = x
        self.__y = y

        self.bounce = 0.85

        super().__init__(x, y, m)

    def tick(self, dt):
        self._updatePosition(dt)
        [c.tick(dt) for c in self.components]

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.frame.x = value
        self.engine.x = value
        self.cooler.x = value
        self.fuel_tank.x = value
        self.cargo_bay.x = value

        if OFFSET:
            GLOBAL_OFFSET[0] = value - 400 + 64/2
        else:
            GLOBAL_OFFSET[0] = 0

        self.__x = value
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.frame.y = value
        self.engine.y = value
        self.cooler.y = value
        self.fuel_tank.y = value
        self.cargo_bay.y = value

        if OFFSET:
            GLOBAL_OFFSET[1] = value - 300 + 64/2
        else:
            GLOBAL_OFFSET[1] = 0
        self.__y = value
        self.landed = False

    def render(self, screen):
        [o.render(screen) for o in self.components]

    def throttle_up(self):
        self.forces_y.append(-self.engine.lift)

    def throttle_down(self):
        self.forces_y.append(self.engine.lift)

    def throttle_left(self):
        self.forces_x.append(-self.engine.side_force)

    def throttle_right(self):
        self.forces_x.append(self.engine.side_force)

    def throttle_horizontal(self, value):
        self.forces_x.append(self.engine.side_force*value)

    def throttle_vertical(self, value):
        self.forces_y.append(self.engine.lift*value)

    def get_hp(self):
        return str(int(self.frame.hp))

    def get_fuel_level(self):
        return str(self.fuel_tank.fuel_level)

    def engine_cooling(self, dt):
        self.engine.temp -= self.cooler.cooling_rate * dt

    def drill_block(self, block_o):
        # Run drill animation:

        # Move to target block:

        # Add mineral to cargo bay:
        # if block_o == mineral
        self.collect_cargo(block_o)

        # Delete mineral:

        # game.gameObjects.remove(mineral_o)

        pass

