from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class Worksheet:
    def __init__(self, file_name: str):
        self.file = canvas.Canvas(file_name)
        # Set page size to American standard
        self.file.setPageSize(letter)
        self.width, self.height = letter

    def draw_page_xy_ruler(self):
        for i in range(0, 11):
            self.file.drawString(
                ((i / 10) * self.width),
                0,
                f"x={i}"
            )
            self.file.drawString(
                0,
                ((i / 10) * self.height),
                f"y={i}")

    def write(self, x: float, y: float, text: str):
        self.file.drawString(x, y, text)

    def next_page(self):
        self.file.showPage()

    def generate_pdf(self):
        self.file.save()
