from worksheet import Worksheet

FULL_WIDTH = 612.0
FULL_HEIGHT = 792.0
RULED_LINE_LENGTH = (61.2, 550.8)
RULED_LINE_WIDTH = 1
RULED_LINE_THICK = 2
DASHED_LINE_FULL_LENGTH = (72, 548)
DASHED_LINE_WIDTH = 1
DASH_LENGTH = (DASHED_LINE_FULL_LENGTH[1] - DASHED_LINE_FULL_LENGTH[0]) / 30
LARGE_SPACE = 60
SMALL_SPACE = 20
TINY_SPACE = 10


class Exercise:
    def __init__(self, file: Worksheet):
        self.worksheet = file
        self.y_space = file.y_space
        file.draw_line(0, self.y_space, file.width, self.y_space)

    def generate_exercises(self):
        self.worksheet.generate_pdf()

    def decrement_y_space(self, val: int):
        self.y_space -= val

    def generate_guideline(self):
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

    def letter_trace_exercise(self):
        self.generate_guideline()
        self.generate_guideline()

    def word_trace_exercise(self):
        pass


if __name__ == "__main__":
    file_ex = Worksheet("file.pdf", logo=True, ruler=False)
    exercises = Exercise(file_ex)
    exercises.letter_trace_exercise()
    exercises.generate_exercises()
