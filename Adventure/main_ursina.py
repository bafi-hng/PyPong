from string import whitespace
from turtle import position
from ursina import *

app = Ursina()

#quit game
def input(key):
    if key == 'escape':
        quit()


class button(Button):
    def __init__(self, position = (0,0), text = 'default'):
        super().__init__(
            parent = scene,
            position = position,
            text = text,
            text_color = color.white,
            color = color.black,
            highlight_color = color.white,
            pressed_color = color.white,
            scale = (3,1)
        )

    def input(self, key):
        if self.hovered:
            self.text_color = color.black
        else:
            self.text_color = color.white


# button1 = Button(position = Vec2(0,0), text = 'Button', 
#             color = color.black,highlight_color = color.white, scale = (0.4,0.1))

button2 = button()

app.run()