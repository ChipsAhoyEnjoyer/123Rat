from PIL import Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
import pathlib


def remove_image_alpha_channels(path):
    # Open the image with transparency (alpha channel)
    image = Image.open(path)

    # Ensure the image is in RGBA format (which includes the alpha channel)
    image = image.convert("RGBA")

    # Create a new image with a solid background color (e.g., white)
    # The background image is the same size as the original image, and fully opaque (255 alpha)
    background_color = (255, 255, 255, 255)  # White color with full opacity
    background = Image.new("RGBA", image.size, background_color)

    # Paste the original image onto the background. The alpha channel is used as a mask.
    background.paste(image, (0, 0), image)  # Use the alpha channel as the mask

    # Now convert the image to RGB (no alpha channel)
    image_no_alpha = background.convert("RGB")

    # Save the image without alpha (transparency)
    image_no_alpha.save(path)

    # Optionally, you can save it as JPG, which doesn't support transparency
    # image_no_alpha.save("image_no_alpha.jpg")


def register_new_font(font_name, font_path):
    pdfmetrics.registerFont(TTFont(font_name, font_path))


def return_asset_path(asset_name: str) -> str:
    working_dir = os.path.split(os.getcwd())[-1]
    if working_dir == "123Rat":
        assets_path = os.path.abspath("assets")
    elif working_dir == "src":
        assets_path = os.path.abspath("../assets")
    else:
        raise FileNotFoundError("Cannot find 'assets' directory")
    return os.path.join(assets_path, asset_name)

def _find_destination() -> str:
    repo_path = pathlib.Path(os.getcwd())
    parts = repo_path.parts
    file_path = parts[0]
    for i in range(len(parts)):
        file_path = os.path.join(str(file_path), parts[i])
        if parts[i] == "123Rat":
            break
    return str(file_path)