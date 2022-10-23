from ursina import *

app = Ursina()

firstEntity = Entity(
    model = 'cube',
    color = color.rgb(255, 0, 0),
    texture = 'brick',
    position = (0,0,0),
    rotation = (0,0,0),
    scale = 2,
)

EditorCamera()


app.run()
