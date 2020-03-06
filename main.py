import pyglet # import the library
win= pyglet.window.Window() # create the window

# Create a sprite
tile= pyglet.image.load('images/assets/ground/grey.png')
spr = pyglet.sprite.Sprite(tile)

def update(dt):
  pass

sprites = []
for i in range(4):
    #sprites.append(pyglet.sprite.Sprite(tile, x = i * 48, y = 0))
    for j in range(4):
        sprites.append(pyglet.sprite.Sprite(tile, x = i * 48, y = j * 50))

# Start the event loop
@win.event
def on_draw():
    win.clear()
    for i in range(16):
        sprites[i].draw()
    # for j in range(4):
    #     sprites[j].draw()

pyglet.clock.schedule(update) 
pyglet.app.run()