from worksheet import Worksheet
import tools
from random import choice, randint
from math import ceil

# Font setup
HINDMYSURU = "Hind_Mysuru_Light"  # Standard font
tools.register_new_font(HINDMYSURU, "../assets/HindMysuru-Light.ttf")
TRACE_FONT = "Trace"  # Trace font
tools.register_new_font(TRACE_FONT, "../assets/Trace.TTF")
GUIDELINE_FONT_SIZE = 45

# Variables for exercises
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Color shape exercise
SHAPES = ("triangle", "square", "circle")

# Trace exercise
WORDS = ("dog", "cat", "spider")
RULED_LINE_LENGTH = (61.2, 550.8)  # TODO: Make this calculate based off page dimensions
RULED_LINE_WIDTH = 0.5  # Thin line
RULED_LINE_WIDTH_THICK = 1  # Thick line
DASHED_LINE_FULL_LENGTH = (72, 548)  # TODO: Make this calculate based off page dimensions
DASHED_LINE_WIDTH = RULED_LINE_WIDTH
DASH_LENGTH = (DASHED_LINE_FULL_LENGTH[1] - DASHED_LINE_FULL_LENGTH[0]) / 30

# Standardized lengths
X_COORD_TO_START_WRITING = 67
LARGE_SPACE = 40
SMALL_SPACE = 20
TINY_SPACE = 10
SHAPE_LENGTH = 50


class Exercise:
    """Base class for exercises to keep track how much estate(y_space) is left on the page"""
    def __init__(self):
        self.file = None
        self.y_space = None

    def generate_exercises(self):
        self.file.generate_pdf()

    def decrement_y_space(self, val: int):
        self.y_space -= val


class ColorShapeExercise(Exercise):
    """
    Create shapes for coloring

    List of available shapes for this exercise in SHAPES variable
    To add more shapes:
    1. Create shape using primitive line drawing methods in worksheet.py to make a new shape method in that file
    2. (optional)Add shape name to SHAPE variable at the top of exercise.py file so that it can be chosen randomly if
       no shape is inputted by the user
    3. Add a case with the shape name and method in the draw_shape method in exercise.py
    """
    def __init__(self, file: Worksheet | Exercise, shape: str = ""):
        super().__init__()
        if isinstance(file, Exercise):
            self.file = file.file
            self.y_space = file.y_space
        elif isinstance(file, Worksheet):
            self.file = file
            self.y_space = file.y_space
        self.shape = shape if shape != "" else choice(SHAPES)
        self.number = randint(11, 20)  # Change these number to ones you want your child to practice
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

    def _set_color_shape_line_settings(self):
        self.file.fill_color(WHITE)
        self.file.line_stroke_color(BLACK)
        self.file.line_width(RULED_LINE_WIDTH_THICK)

    def _instruction_setup(self):
        instructions = f"Color {self.number} {self.shape}s"
        self.decrement_y_space(TINY_SPACE + GUIDELINE_FONT_SIZE)
        self.file.font_settings(GUIDELINE_FONT_SIZE, HINDMYSURU, BLACK)
        self.file.write(X_COORD_TO_START_WRITING, self.y_space, instructions)

    def num_shapes_per_y_levels(self) -> int:
        max_shapes_per_y_space = 5
        if self.number <= 5:
            return 5
        while max_shapes_per_y_space > 1:
            if self.number % max_shapes_per_y_space == 0:
                return max_shapes_per_y_space
            max_shapes_per_y_space -= 1
        return 5

    def round_number_of_shapes(self):
        """
        Rounds up to the nearest nth(base) number; If you want to color 5/6/7 shapes, it will generate 10 shapes. We
        have extra shapes so that children stop coloring after they get to that number of shapes colored.
        """
        base = 5
        if self.number % base == 0:
            return self.number + base
        return base * (ceil(self.number / base))

    def draw_shapes(self, number_of_y_levels: int, num_of_shapes: int, shapes_per_y_level: int):
        self.decrement_y_space(TINY_SPACE)
        current_x = 0
        shapes_left = num_of_shapes
        for _ in range(number_of_y_levels):
            self.decrement_y_space(TINY_SPACE + SHAPE_LENGTH)
            x_spacing = self.file.width * (1 / min(shapes_per_y_level + 1, shapes_left + 1))
            for _ in range(shapes_per_y_level):
                if shapes_left:
                    current_x += x_spacing
                    self.draw_shape(current_x)
                    shapes_left -= 1
                else:
                    break
            current_x = 0

    def color_shape_exercise(self):
        self._set_color_shape_line_settings()
        self._instruction_setup()
        shapes_per_y_level = self.num_shapes_per_y_levels()
        num_of_shapes = self.round_number_of_shapes()
        number_of_y_levels = ceil(num_of_shapes / shapes_per_y_level)
        self.draw_shapes(number_of_y_levels, num_of_shapes, shapes_per_y_level)


class LetterTraceExercise(Exercise):
    """
    Letter trace exercise. We trace letters/words here, keep up
    """
    def __init__(self, file, chars: str = ""):
        super().__init__()
        if isinstance(file, Exercise):
            self.file = file.file
            self.y_space = file.y_space
        elif isinstance(file, Worksheet):
            self.file = file
            self.y_space = file.y_space
        if self.file is None:
            raise ValueError(
                "LetterTraceExercise type objects only take accept Worksheet or Exercise type objects as files"
            )
        self.chars = chars if chars != "" else choice(WORDS)
        self.letter_trace_exercise()

    def generate_guideline(self):
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

    def generate_traceable_word(self):
        """
        MUST come after the generate_guideline method
        This method does not decrement y space because it will overlap a guideline
        """
        self.file.font_settings(
            font_size=GUIDELINE_FONT_SIZE,
            font=TRACE_FONT,
            rgb=BLACK
        )
        formatted_chars = f"{self.chars} {self.chars} {self.chars}"
        self.file.write(X_COORD_TO_START_WRITING, self.y_space, formatted_chars)

    def letter_trace_exercise(self):
        self.file.font_settings(
            font_size=GUIDELINE_FONT_SIZE,
            font=HINDMYSURU,
            rgb=BLACK
        )
        self.decrement_y_space(LARGE_SPACE)
        self.file.write(RULED_LINE_LENGTH[0] + 5, self.y_space, self.chars.capitalize())
        self.generate_guideline()
        self.generate_traceable_word()
        self.generate_guideline()

# TODO: add Testing
# TODO: make shapes smaller and more huddled
# TODO: make is so that the each exercise has a y_space requirement and that you can't draw past the page
# TODO: add another exercise subclass, maybe (Match the word with the picture) or (Addition/Subtraction)