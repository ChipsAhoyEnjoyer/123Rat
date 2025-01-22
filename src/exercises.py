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
    def __init__(self):
        self.file = None
        self.y_space = None

    def generate_exercises(self):
        self.file.generate_pdf()

    def decrement_y_space(self, val: int):
        self.y_space -= val


class ColorShapeExercise(Exercise):
    def __init__(self, file: Worksheet | Exercise, shape: str | None = None, number: int | None = None):
        super().__init__()
        if isinstance(file, Exercise):
            self.file = file.file
            self.y_space = file.y_space
        elif isinstance(file, Worksheet):
            self.file = file
            self.y_space = file.y_space
        self.shape = shape if shape is not None else choice(SHAPES)
        self.number = number if number is not None else randint(5, 20)
        self.color_shape_exercise()

    def draw_shape(self, x: float):
        match self.shape:
            case "square":
                self.file.draw_rect(x - (SHAPE_LENGTH / 2), self.y_space, SHAPE_LENGTH, SHAPE_LENGTH)
            case "circle":
                self.file.draw_circle(x, self.y_space + (SHAPE_LENGTH / 2), SHAPE_LENGTH / 2)
            case "triangle":
                self.file.draw_triangle(x - (SHAPE_LENGTH / 2), self.y_space, SHAPE_LENGTH)
            case _:
                raise ValueError("Invalid shape; Shape not registered")

    def color_shape_exercise(self):
        self.file.fill_color(WHITE)
        self.file.line_stroke_color(BLACK)
        self.file.line_width(RULED_LINE_WIDTH_THICK)

        max_shapes_per_y_space = 5
        num_of_shapes = self.number

        number_of_y_levels = ceil(num_of_shapes / max_shapes_per_y_space)
        shapes_per_y_level = min(num_of_shapes, max_shapes_per_y_space)
        x_spacing = self.file.width * (1 / (shapes_per_y_level + 1))
        current_x = 0
        shapes_left = num_of_shapes
        for _ in range(number_of_y_levels):
            self.decrement_y_space(TINY_SPACE + SHAPE_LENGTH)
            for _ in range(shapes_per_y_level):
                if shapes_left:
                    current_x += x_spacing
                    self.draw_shape(current_x)
                    shapes_left -= 1
                else:
                    break
            current_x = 0


class LetterTraceExercise(Exercise):
    def __init__(self, file, chars: str = None):
        super().__init__()
        if isinstance(file, Exercise):
            self.file = file.file
            self.y_space = file.y_space
        elif isinstance(file, Worksheet):
            self.file = file
            self.y_space = file.y_space
        if self.file is None:
            raise ValueError("Wrong class type")
        self.chars = chars
        self.letter_trace_exercise()

    def generate_guideline(self, traceable: bool = False):
        x1, x2 = RULED_LINE_LENGTH
        self.file.line_width(RULED_LINE_WIDTH_THICK)
        self.file.draw_line(x1, (self.y_space - TINY_SPACE), x2, (self.y_space - TINY_SPACE))
        self.decrement_y_space(TINY_SPACE)

        dash_x1, dash_x2 = DASHED_LINE_FULL_LENGTH
        self.file.line_width(DASHED_LINE_WIDTH)
        self.file.draw_dashed(
            dash_len=DASH_LENGTH,
            gap_len=DASH_LENGTH,
            start_x=dash_x1,
            end_x=dash_x2,
            start_y=self.y_space - SMALL_SPACE,
            end_y=self.y_space - SMALL_SPACE
        )
        self.decrement_y_space(SMALL_SPACE)

        self.file.line_width(RULED_LINE_WIDTH_THICK)
        self.file.draw_line(x1, (self.y_space - SMALL_SPACE), x2, (self.y_space - SMALL_SPACE))
        self.decrement_y_space(SMALL_SPACE)

        if traceable:
            self.file.font_settings(
                font_size=GUIDELINE_FONT_SIZE,
                font=TRACE_FONT,
                rgb=BLACK
            )
            formatted_chars = f"{self.chars} {self.chars} {self.chars}"
            self.file.write(RULED_LINE_LENGTH[0] + 5, self.y_space, formatted_chars)

    def letter_trace_exercise(self):
        if self.chars:
            self.file.font_settings(
                font_size=GUIDELINE_FONT_SIZE,
                font=HINDMYSURU,
                rgb=BLACK
            )
            self.decrement_y_space(LARGE_SPACE)
            self.file.write(RULED_LINE_LENGTH[0] + 5, self.y_space, self.chars)
        self.generate_guideline(True)
        self.generate_guideline()


if __name__ == "__main__":
    file_ex = Worksheet("file.pdf", logo=True, ruler=False)
    exercises = LetterTraceExercise(file_ex, "Dog")
    exercises = ColorShapeExercise(exercises)
    exercises.generate_exercises()

# TODO: add Testing
# TODO: add Tkinter UI
# TODO: make logo prettier
# TODO: make shapes smaller and more huddled
# TODO: last row of shapes should centered