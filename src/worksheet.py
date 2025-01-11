from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image


LOGO_PATH = "../assets/rat.png"
LOGO = (155, 712, "123Rat")
TITLE = "123Rat WorkSheet"


class Worksheet:
    def __init__(self, file_name: str, draw_ruler: bool = False):
        self.file = canvas.Canvas(file_name)
        self.width = None
        self.height = None
        self._page_setup()

        self._draw_logo()
        if draw_ruler:
            self._draw_page_xy_ruler()

    def set_title(self, title: str):
        self.file.setTitle(title)

    def write(self, x: float, y: float, text: str):
        self.file.drawString(x, y, text)

    def next_page(self):
        self.file.showPage()

    def generate_pdf(self):
        self.file.save()

    def draw_line(self, x1: float, y1: float, x2: float, y2: float):
        self.file.line(x1, y1, x2, y2)

    def draw_dashed(self, line_len: int | list, space_len: int):
        self.file.setDash(line_len, space_len)

    def draw_image(self, path, x: float, y: float):
        self.file.drawImage(
            path,
            x,
            y,
        )

    def _draw_page_xy_ruler(self):
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

    def _draw_logo(self):
        img = Image.open(LOGO_PATH)
        self.draw_image(
            LOGO_PATH,
            0,
            (self.height - img.height)
        )

        self.write(*LOGO)

    def _page_setup(self):
        # Set page size to American standard
        self.file.setPageSize(letter)
        self.width, self.height = letter

        self.set_title(TITLE)
        self._draw_logo()

# TODO: setup dashed lines(canvas.setDash(self, array=[], phase=0))
# TODO: setup line width, fonts and font sizes for different methods
# TODO: create a method to turn on page ruler
# TODO: create exercises

