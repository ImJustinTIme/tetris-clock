import time
import os
import board, sys
import displayio
from digitalio import DigitalInOut, Pull
from adafruit_matrixportal.matrix import Matrix
from adafruit_debouncer import Debouncer

DEFAULT_FRAME_DURATION = 0.08  # 100ms
BLINK = True
DEBUG = False
current_image = None
current_frame = 0
current_loop = 0
frame_count = 0
frame_duration = DEFAULT_FRAME_DURATION
TILE_HEIGHT = 42


def initiate_bmps(sprite_group):
    """
    Load an image as a sprite
    """
    # pylint: disable=global-statement
    global current_frame, current_loop, frame_count, frame_duration
    while sprite_group:
        sprite_group.pop()

    CA = open("/bmps/CA.bmp", "rb")
    N0 = open("/bmps/N0A.bmp", "rb")
    N1 = open("/bmps/N1A.bmp", "rb")
    N2 = open("/bmps/N2A.bmp", "rb")
    # N3 = open('/bmps/N3A.bmp', "rb")
    # N4 = open('/bmps/N4A.bmp', "rb")
    # N5 = open('/bmps/N5A.bmp', "rb")
    N6 = open("/bmps/N6A.bmp", "rb")
    # N7 = open('/bmps/N7A.bmp', 'rb')
    # N8 = open('/bmps/N8A.bmp', 'rb')
    # N9 = open('/bmps/N9A.bmp', 'rb')

    # CircuitPython 6 & 7 compatible
    bitmapN2 = displayio.OnDiskBitmap(N2)
    #   bitmapCA = displayio.OnDiskBitmap(CA)
    #   bitmapN0 = displayio.OnDiskBitmap(N0)
    #   bitmapN1 = displayio.OnDiskBitmap(N1)
    sprite = displayio.TileGrid(
        bitmap=bitmapN2,
        pixel_shader=getattr(bitmapN2, "pixel_shader", displayio.ColorConverter()),
        tile_width=bitmapN2.width,
        tile_height=TILE_HEIGHT,
        x=10,
    )

    # # CircuitPython 7+ compatible
    # bitmap = displayio.OnDiskBitmap(filename)
    # sprite = displayio.TileGrid(
    #     bitmap,
    #     pixel_shader=bitmap.pixel_shader,
    #     tile_width=bitmap.width,
    #     tile_height=matrix.display.height,
    # )

    sprite_group.append(sprite)

    current_frame = 0
    current_loop = 0
    frame_count = int(bitmap.height / TILE_HEIGHT)
    frame_duration = DEFAULT_FRAME_DURATION


def advance_frame(sprite_group):
    """
    Advance to the next frame and loop back at the end
    """
    # pylint: disable=global-statement
    global current_frame, current_loop
    current_frame = current_frame + 1
    if current_frame >= frame_count:
        current_frame = 0
        current_loop = current_loop + 1
    sprite_group[0][0] = current_frame


def DigitTest(sprite_group, display, matrix, network):
    # --- Display setup ---
    matrix.display.show(sprite_group)

    initiate_bmps(sprite_group)
    sprite_group[0][0] = 90
    while True:
        #   advance_frame(sprite_group)
        time.sleep(frame_duration)
