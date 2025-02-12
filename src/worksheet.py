from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import tools


LOGO = (155, 712, "123Rat")
LOGO_FONT_SIZE = 36
TITLE = "123Rat WorkSheet"
FONT_SIZE = 20

# Assets

LOGO_FONT = "comic_sans"
LOGO_PATH = tools.return_asset_path("rat.png")
COMIC_SANS_PATH = tools.return_asset_path("ComicSansMS.ttf")
tools.register_new_font(LOGO_FONT, font_path=COMIC_SANS_PATH)


class Worksheet:
    """
    Class used to manipulate reportlab Canvas class because CamelCase is not pythonic *hiss*

    Definitely not my notes from skimming the docs
    """
    def __init__(self, file_name: str, logo: bool = True, ruler: bool = False):
        self.file = canvas.Canvas(file_name, pagesize=letter)
        self.logo = logo
        self.ruler = ruler
        self.width, self.height = letter
        self.y_space = self.height
        self._page_setup()

    def set_title(self, title: str):
        self.file.setTitle(title)

    def font_settings(self, font_size: float, font: str = None, rgb: tuple[float, float, float] = None):
        if rgb:
            self.fill_color(rgb)
        if not font:
            self.file.setFontSize(font_size)
            return
        self.file.setFont(font, font_size)

    def fill_color(self, rgb: tuple[float, float, float]):
        self.file.setFillColorRGB(*rgb)

    def line_stroke_color(self, rgb: tuple[float, float, float]):
        self.file.setStrokeColorRGB(*rgb)

    def line_width(self, width: float):
        self.file.setLineWidth(width)

    def write(self, x: float, y: float, text: str):
        self.file.drawString(x, y, text)

    def next_page(self):
        self.file.showPage()

    def generate_pdf(self):
        self.file.save()

    def draw_line(self, x1: float, y1: float, x2: float, y2: float):
        self.file.line(x1, y1, x2, y2)

    def draw_dashed(
            self, dash_len: float,
            gap_len: float,
            start_x: float,
            start_y: float,
            end_x: float,
            end_y: float,
    ):
        self.file.setDash(dash_len, gap_len)
        self.draw_line(start_x, start_y, end_x, end_y)
        self.file.setDash()  # reset lines so no more dashes

    def draw_rect(self, x: float, y: float, width: float, height: float):
        self.file.rect(x, y, width, height)

    def draw_circle(self, x: float, y: float, rad: float):
        self.file.circle(x, y, rad)

    def draw_triangle(self, x: float, y: float, side_len: float):
        self.draw_line(x, y, x + side_len, y)
        self.draw_line(x, y, x + (side_len / 2), y + side_len)
        self.draw_line(x + side_len, y, x + (side_len / 2), y + side_len)

    def draw_image(self, path, x: float, y: float):
        self.file.drawImage(
            path,
            x,
            y,
        )

    def _draw_page_xy_ruler(self):
        """
        Draw x and y lines on the page for easier plotting
        """
        for i in range(1, 11):
            self.file.drawString(
                ((i / 10) * self.width),
                0,
                f"x={((i / 10) * self.width)}"
            )
            self.file.line(
                ((i / 10) * self.width),
                0,
                ((i / 10) * self.width),
                self.height
            )

            self.file.drawString(
                0,
                ((i / 10) * self.height),
                f"y={((i / 10) * self.height)}"
            )
            self.file.line(
                0,
                ((i / 10) * self.height),
                self.width,
                ((i / 10) * self.height))

    def _draw_logo(self) -> int:
        img = Image.open(LOGO_PATH)
        self.draw_image(
            LOGO_PATH,
            0,
            (self.height - img.height)
        )
        self.write(*LOGO)
        return img.height

    def _page_setup(self):
        # Set page size to American standard
        self.font_settings(LOGO_FONT_SIZE, LOGO_FONT)
        self.set_title(TITLE)
        if self.logo:
            logo_height = self._draw_logo()
            self.y_space -= logo_height
        if self.ruler:
            self.font_settings(12)
            self._draw_page_xy_ruler()  # Page ruler to help with mapping
        self.font_settings(FONT_SIZE)
