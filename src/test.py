from worksheet import Worksheet, FONT


class TestWorksheet:
    def __init__(self, filename: str):
        self.test = Worksheet(filename, logo=False)

    def test_write_fill_color(self):
        self.test.font_settings(
            6,
            FONT,
            (255, 0, 0)
        )

        self.test.write(
            100,
            100,
            "Testing"
        )

    def test_draw_line(self):
        x1, y1, x2, y2 = 0, self.test.height, self.test.width, 0
        self.test.draw_line(x1, y1, x2, y2)

    def test_draw_dashed(self):
        x1, y1, x2, y2 = 0, 0, self.test.width, self.test.height
        self.test.draw_dashed(1, 1, x1, y1, x2, y2)

    def test_line_fill_color(self):
        self.test.line_stroke_color((255, 0, 0))
        x1, y1, x2, y2 = 0, (self.test.height / 2), self.test.width, (self.test.height / 2)
        self.test.draw_line(x1, y1, x2, y2)

    def text_draw_image(self):
        path = None
        x = self.test.width / 2
        y = self.test.height / 2
        if path:
            self.test.draw_image(path, x, y)


def main():
    test = TestWorksheet("test_worksheet.pdf")
    test.test_write_fill_color()
    test.test_draw_line()
    test.test_draw_dashed()
    test.test_line_fill_color()
    test.test.generate_pdf()


if __name__ == "__main__":
    main()
