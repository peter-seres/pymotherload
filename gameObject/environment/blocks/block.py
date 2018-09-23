from gameObject.staticGameObject import StaticGameObject


class Block(StaticGameObject):
    def __init__(self, x, y, imgPath, value, density, center):

        if imgPath != "empty":
            super().__init__(imgPath, x, y)

        self.value = value
        self.density = density
        self.center = center
