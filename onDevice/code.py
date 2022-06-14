import board, displayio, terminalio, adafruit_imageload, time, sys
from adafruit_matrixportal.matrix import Matrix

sys.path.insert(0, '/clockFace/')

from clockFace.basic_test import BasicTest
from clockFace.animation_test import AnimationTest

matrix = Matrix(width=64, height=64 )
display = matrix.display
group = displayio.Group()

#BasicTest(group, display, matrix)
AnimationTest(group, display, matrix)

# parrot_bit, parrot_pal = adafruit_imageload.load("/partyParrotsTweet.bmp",
#                                                  bitmap=displayio.Bitmap,
#                                                  palette=displayio.Palette)

# parrot_grid = displayio.TileGrid(parrot_bit, pixel_shader=parrot_pal,
#                                  width=1, height=1,
#                                  tile_height=32, tile_width=32,
#                                  default_tile=1,
#                                  x=0, y=0)

# group.append(parrot_grid)

# display.show(group)

# party = 0
# p = 0

# while True:
#   if (party + 0.1) < time.monotonic():
#     parrot_grid[0] = p
#     p += 1
#     party = time.monotonic()
#     if p > 9:
#       p = 0
