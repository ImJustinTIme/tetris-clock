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

sprites = {}
currentTime = []


def initiate_bmps(sprite_group, timeLib):
    """
    Load an image as a sprite
    """
    # pylint: disable=global-statement
    global current_frame, current_loop, frame_count, frame_duration
    while sprite_group:
        sprite_group.pop()

    files = [
        open("/bmps/N0A.bmp", "rb"),
        open("/bmps/N1A.bmp", "rb"),
        open("/bmps/N2A.bmp", "rb"),
        open("/bmps/N3A.bmp", "rb"),
        open("/bmps/N4A.bmp", "rb"),
        open("/bmps/N5A.bmp", "rb"),
        open("/bmps/N6A.bmp", "rb"),
        open("/bmps/N7A.bmp", "rb"),
        open("/bmps/N9A.bmp", "rb"),
        open("/bmps/N9A.bmp", "rb"),
        open("/bmps/CA.bmp", "rb"),
    ]

    for index, file in enumerate(files):
        bitMap = displayio.OnDiskBitmap(file)
        frameLength = int(bitMap.height / TILE_HEIGHT)
        sprites[index] = {"file": file, "bitMap": bitMap, "frameLength": frameLength}

    print("width")
    print(f"sprites[10]['bitMap'].width: {sprites[10]['bitMap'].width}")
    print(f"sprites[0]['bitMap'].width: {sprites[0]['bitMap'].width}")
    # for 4 bit time

    sprite0 = displayio.TileGrid(
        bitmap=sprites[1]["bitMap"],
        pixel_shader=getattr(
            sprites[1]["bitMap"], "pixel_shader", displayio.ColorConverter()
        ),
        tile_width=sprites[1]["bitMap"].width,
        tile_height=TILE_HEIGHT,
        x=1,
    )
    sprite1 = displayio.TileGrid(
        bitmap=sprites[1]["bitMap"],
        pixel_shader=getattr(
            sprites[1]["bitMap"], "pixel_shader", displayio.ColorConverter()
        ),
        tile_width=sprites[1]["bitMap"].width,
        tile_height=TILE_HEIGHT,
        x=15,
    )
    spriteCA = displayio.TileGrid(
        bitmap=sprites[10]["bitMap"],
        pixel_shader=getattr(
            sprites[10]["bitMap"], "pixel_shader", displayio.ColorConverter()
        ),
        tile_width=sprites[10]["bitMap"].width,
        tile_height=TILE_HEIGHT,
        x=28,
    )
    sprite2 = displayio.TileGrid(
        bitmap=sprites[4]["bitMap"],
        pixel_shader=getattr(
            sprites[4]["bitMap"], "pixel_shader", displayio.ColorConverter()
        ),
        tile_width=sprites[4]["bitMap"].width,
        tile_height=TILE_HEIGHT,
        x=35,
    )
    sprite3 = displayio.TileGrid(
        bitmap=sprites[5]["bitMap"],
        pixel_shader=getattr(
            sprites[5]["bitMap"], "pixel_shader", displayio.ColorConverter()
        ),
        tile_width=sprites[5]["bitMap"].width,
        tile_height=TILE_HEIGHT,
        x=49,
    )

    sprite_group.append(sprite0)
    sprite_group.append(sprite1)
    sprite_group.append(sprite2)
    sprite_group.append(sprite3)
    sprite_group.append(spriteCA)

    current_frame = 0
    current_loop = 0
    frame_count = sprites[10]["frameLength"]
    frame_duration = DEFAULT_FRAME_DURATION


def advance_frame(sprite_group):
    """
    Advance to the next frame and loop back at the end

    TODO: this needs to be change so that is called on each digit not just for the sprite_group
        - also need to make it so it animates until out of frames some how. each one has a different lenght
    """
    # pylint: disable=global-statement
    global current_frame, current_loop
    current_frame = current_frame + 1

    if current_frame >= frame_count:
        current_frame = 0
        current_loop = current_loop + 1

    # for each tile added to sprite_group advace y section by 1 
    # if not animated yet this will break things 
    sprite_group[0][0] = 65
    sprite_group[1][0] = 65
    sprite_group[4][0] = 60



def AnimationTest(sprite_group, display, matrix, network):
    # --- Display setup ---
    matrix.display.show(sprite_group)

    initiate_bmps(sprite_group, network.get_local_time())
    advance_frame(sprite_group)
    while True:
        # advance_frame(sprite_group)
        time.sleep(frame_duration)
