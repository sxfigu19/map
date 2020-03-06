import pyglet # import the library
win= pyglet.window.Window() # create the window

# Create a sprite
tilegrey= pyglet.image.load('images/assets/ground/grey.png')
spr1 = pyglet.sprite.Sprite(tilegrey)
tileblue= pyglet.image.load('images/assets/ground/blue.png')
spr2 = pyglet.sprite.Sprite(tileblue)
tilewhite= pyglet.image.load('images/assets/ground/white.png')
spr3 = pyglet.sprite.Sprite(tilewhite)

def update(dt):
  pass

grey = []
for i in range(14):
    for j in range(10):
        grey.append(pyglet.sprite.Sprite(tilegrey, x = i * 48, y = j * 50))

blue = []
for i in range(14):
    for j in range(5):
        blue.append(pyglet.sprite.Sprite(tileblue, x = i * 48, y = j * 150))

white = []
for i in range(14):
    for j in range(5):
        white.append(pyglet.sprite.Sprite(tilewhite, x = i * 144, y = j * 100))

# Start the event loop
@win.event
def on_draw():
    win.clear()
    for i in range(140):
        grey[i].draw()
    for i in range(70):
        blue[i].draw()
    for i in range(70):
        white[i].draw()
    


pyglet.clock.schedule(update) 
pyglet.app.run()