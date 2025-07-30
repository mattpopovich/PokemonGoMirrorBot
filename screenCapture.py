import subprocess
from PIL import ImageGrab


def capture_screen():
    # tiff is faster than png
    #   https://stackoverflow.com/a/13024603/4368898
    # -x for no sound effects
    subprocess.run(["screencapture", "-t", "tiff", "-x", "/tmp/screen.tiff"])


# def get_pixel_color(coordinate: list[int]) -> list[int]:
#     """Get the pixel color at a [x,y] coordinate."""
#     capture_screen()
#     x, y = coordinate
#     with Image.open('/tmp/screen.tiff') as img:
#         img = img.convert('RGB')  # Convert to RGB mode
#         colors: tuple = img.getpixel((x, y))
#         return list(colors)


def get_pixel_color(coordinate: list[int]) -> list[int]:
    """Get the pixel color at a [x,y] coordinate."""
    # Take a screenshot using ImageGrab
    screenshot = ImageGrab.grab()

    # Convert the screenshot to RGB mode to ensure 3 dimensions
    screenshot_rgb = screenshot.convert("RGB")

    # Get the pixel color at the specified (x, y) coordinate
    color: tuple = screenshot_rgb.getpixel(coordinate)
    return list(color)
