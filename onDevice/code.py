from clockFace.basic_test import BasicTest
from clockFace.animation_test import AnimationTest
from clockFace.digit_test import DigitTest
from clockFace.clock_v1 import ClockV1

import board, displayio, terminalio, adafruit_imageload, time, sys
from adafruit_matrixportal.matrix import Matrix
from adafruit_matrixportal.network import Network

sys.path.insert(0, "/clockFace/")


try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("Time will be set for {}".format(secrets["timezone"]))
network = Network(status_neopixel=board.NEOPIXEL, debug=False)
matrix = Matrix(width=64, height=64)
display = matrix.display
group = displayio.Group()

# BasicTest(group, display, matrix, network)
ClockV1(group, display, matrix, network)
# DigitTest(group, display, matrix, network);
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
