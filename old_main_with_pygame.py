from gameObject.interface.text_display import TextObject
from gameObject.tank.tank import Tank
from gameEngine02 import gameEngine02

tank = Tank(400, 100, 0.1)

# Define: terrain, Terrain class, procedural generation.

game = gameEngine02(800, 600, tank)
hp_display = TextObject(50, 500, font_size=21, text="HP:")
fuel_display = TextObject(50, 475, font_size=21, text="Fuel:")
quit_display = TextObject(2, 5, font_size=14, text="ESC = QUIT")
w_display = TextObject(2, 20, font_size=14, text="W = up")
a_display = TextObject(2, 35, font_size=14, text="A = left")
s_display = TextObject(2, 50, font_size=14, text="S = down")
d_display = TextObject(2, 65, font_size=14, text="D = right")

game.interfaceObjects.extend([hp_display, fuel_display, quit_display, w_display, a_display, s_display, d_display])

for gameStatus in game.mainloop():
    pass
