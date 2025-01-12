from worksheet import Worksheet


class TestWorksheet:
    def __init__(self, filename: str):
        self.test = Worksheet(filename)

    def test_write(self):
        pass

    def test_draw_line(self):
        pass

    def test_draw_dashed(self):
        x1, y1, x2, y2 = 0, 0, self.test.width, self.test.height
        # Diagonal dashed line from bottom left to top right
        self.test.draw_dashed(1, 1, x1, y1, x2, y2)

    def test_draw_image(self):
        pass

    def test_font_sizes_and_fonts(self):
        pass


def main():
    test = TestWorksheet("test_worksheet")
    test.test_write()
    test.test_draw_line()
    test.test_draw_dashed()
    test.test_draw_image()
    test.test_font_sizes_and_fonts()
    test.test.generate_pdf()
    return 0


if __name__ == "__test__":
    main()
