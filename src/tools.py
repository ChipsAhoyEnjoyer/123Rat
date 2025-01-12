from PIL import Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


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
