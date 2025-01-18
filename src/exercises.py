from worksheet import Worksheet
import tools

HINDMYSURU = "Hind_Mysuru_Light"
tools.register_new_font(HINDMYSURU, "../assets/HindMysuru-Light.ttf")
TRACE_FONT = "Trace"
tools.register_new_font(TRACE_FONT, "../assets/Trace.TTF")
GUIDELINE_FONT_SIZE = 45
BLACK_RGB = (0, 0, 0)

FULL_WIDTH = 612.0
FULL_HEIGHT = 792.0
RULED_LINE_LENGTH = (61.2, 550.8)
RULED_LINE_WIDTH = 0.5
RULED_LINE_THICK = 1
DASHED_LINE_FULL_LENGTH = (72, 548)
DASHED_LINE_WIDTH = 0.5
DASH_LENGTH = (DASHED_LINE_FULL_LENGTH[1] - DASHED_LINE_FULL_LENGTH[0]) / 30
LARGE_SPACE = 40
SMALL_SPACE = 20
TINY_SPACE = 10


class Exercise:
    def __init__(self, file: Worksheet):
        self.worksheet = file
        self.y_space = file.y_space
        # file.draw_line(0, self.y_space, file.width, self.y_space)

    def generate_exercises(self):
        self.worksheet.generate_pdf()

    def decrement_y_space(self, val: int):
        self.y_space -= val

    def generate_guideline(self, chars: str = None):
        x1, x2 = RULED_LINE_LENGTH
        self.worksheet.line_width(RULED_LINE_THICK)
        self.worksheet.draw_line(x1, (self.y_space - TINY_SPACE), x2, (self.y_space - TINY_SPACE))
        self.decrement_y_space(TINY_SPACE)

        dash_x1, dash_x2 = DASHED_LINE_FULL_LENGTH
        self.worksheet.line_width(DASHED_LINE_WIDTH)
        self.worksheet.draw_dashed(
            dash_len=DASH_LENGTH,
            gap_len=DASH_LENGTH,
            start_x=dash_x1,
            end_x=dash_x2,
            start_y=self.y_space - SMALL_SPACE,
            end_y=self.y_space - SMALL_SPACE
        )
        self.decrement_y_space(SMALL_SPACE)

        self.worksheet.line_width(RULED_LINE_THICK)
        self.worksheet.draw_line(x1, (self.y_space - SMALL_SPACE), x2, (self.y_space - SMALL_SPACE))
        self.decrement_y_space(SMALL_SPACE)

        if chars:
            self.worksheet.font_settings(
                font_size=GUIDELINE_FONT_SIZE,
                font=TRACE_FONT,
                rgb=BLACK_RGB
            )
            formatted_chars = f"{chars} {chars} {chars}"
            self.worksheet.write(RULED_LINE_LENGTH[0] + 5, self.y_space, formatted_chars)

    def letter_trace_exercise(self, letter: str):
        self.worksheet.font_settings(
            font_size=GUIDELINE_FONT_SIZE,
            font=HINDMYSURU,
            rgb=BLACK_RGB
        )
        self.decrement_y_space(LARGE_SPACE)
        self.worksheet.write(RULED_LINE_LENGTH[0] + 5, self.y_space, letter)
        self.generate_guideline(letter)
        self.generate_guideline()


if __name__ == "__main__":
    file_ex = Worksheet("file.pdf", logo=True, ruler=False)
    exercises = Exercise(file_ex)
    exercises.letter_trace_exercise("Cat")
    exercises.letter_trace_exercise("Dog")
    exercises.generate_exercises()

# TODO: add a coloring exercise