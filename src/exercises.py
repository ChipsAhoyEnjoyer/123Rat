from worksheet import Worksheet
import tools
from random import choice, randint
from math import ceil

HINDMYSURU = "Hind_Mysuru_Light"
tools.register_new_font(HINDMYSURU, "../assets/HindMysuru-Light.ttf")
TRACE_FONT = "Trace"
tools.register_new_font(TRACE_FONT, "../assets/Trace.TTF")
GUIDELINE_FONT_SIZE = 45
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHAPES = ("triangle", "square", "circle")

FULL_WIDTH = 612.0
FULL_HEIGHT = 792.0
RULED_LINE_LENGTH = (61.2, 550.8)
RULED_LINE_WIDTH = 0.5
RULED_LINE_WIDTH_THICK = 1
DASHED_LINE_FULL_LENGTH = (72, 548)
DASHED_LINE_WIDTH = 0.5
DASH_LENGTH = (DASHED_LINE_FULL_LENGTH[1] - DASHED_LINE_FULL_LENGTH[0]) / 30
LARGE_SPACE = 40
SMALL_SPACE = 20
TINY_SPACE = 10
SHAPE_LENGTH = 50


class Exercise:
    def __init__(self, file: Worksheet):
        self.worksheet = file
        self.y_space = file.y_space
        # file.draw_line(0, self.y_space, file.width, self.y_space)

    def generate_exercises(self):
        self.worksheet.generate_pdf()

    def decrement_y_space(self, val: int):
        self.y_space -= val

    def draw_shape(self, x: float, shape: str):
        match shape:
            case "square":
                self.worksheet.draw_rect(x - (SHAPE_LENGTH / 2), self.y_space, SHAPE_LENGTH, SHAPE_LENGTH)
            case "circle":
                self.worksheet.draw_circle(x, self.y_space + (SHAPE_LENGTH / 2), SHAPE_LENGTH / 2)
            case "triangle":
                self.worksheet.draw_triangle(x - (SHAPE_LENGTH / 2), self.y_space, SHAPE_LENGTH)
            case _:
                raise ValueError("Invalid shape; Shape not registered")

    def color_shape_exercise(self, val: int = None):
        self.worksheet.fill_color(WHITE)
        self.worksheet.line_stroke_color(BLACK)
        self.worksheet.line_width(RULED_LINE_WIDTH_THICK)

        shape = choice(SHAPES)
        max_shapes_per_y_space = 5
        if val is not None:
            num_of_shapes = val
        else:
            num_of_shapes = randint(5, 20)

        number_of_y_levels = ceil(num_of_shapes / max_shapes_per_y_space)
        shapes_per_y_level = min(num_of_shapes, max_shapes_per_y_space)
        x_spacing = self.worksheet.width * (1 / (shapes_per_y_level + 1))
        current_x = 0
        shapes_left = num_of_shapes
        for _ in range(number_of_y_levels):
            self.decrement_y_space(TINY_SPACE + SHAPE_LENGTH)
            for _ in range(shapes_per_y_level):
                if shapes_left:
                    current_x += x_spacing
                    self.draw_shape(current_x, shape)
                    shapes_left -= 1
                else:
                    return
            current_x = 0




    def generate_guideline(self, chars: str = None):
        x1, x2 = RULED_LINE_LENGTH
        self.worksheet.line_width(RULED_LINE_WIDTH_THICK)
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

        self.worksheet.line_width(RULED_LINE_WIDTH_THICK)
        self.worksheet.draw_line(x1, (self.y_space - SMALL_SPACE), x2, (self.y_space - SMALL_SPACE))
        self.decrement_y_space(SMALL_SPACE)

        if chars:
            self.worksheet.font_settings(
                font_size=GUIDELINE_FONT_SIZE,
                font=TRACE_FONT,
                rgb=BLACK
            )
            formatted_chars = f"{chars} {chars} {chars}"
            self.worksheet.write(RULED_LINE_LENGTH[0] + 5, self.y_space, formatted_chars)

    def letter_trace_exercise(self, letter: str):
        self.worksheet.font_settings(
            font_size=GUIDELINE_FONT_SIZE,
            font=HINDMYSURU,
            rgb=BLACK
        )
        self.decrement_y_space(LARGE_SPACE)
        self.worksheet.write(RULED_LINE_LENGTH[0] + 5, self.y_space, letter)
        self.generate_guideline(letter)
        self.generate_guideline()


if __name__ == "__main__":
    file_ex = Worksheet("file.pdf", logo=True, ruler=False)
    exercises = Exercise(file_ex)
    exercises.color_shape_exercise(8)
    exercises.generate_exercises()

# TODO: add a coloring exercise