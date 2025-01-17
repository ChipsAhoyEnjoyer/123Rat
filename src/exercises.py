from worksheet import Worksheet


class Exercise:
    def __init__(self, file: Worksheet):
        y_space = file.y_space
        file.draw_line(0, y_space, file.width, y_space)
        file.generate_pdf()


if __name__ == "__main__":
    file_ex = Worksheet("file.pdf", logo=True)
    exercises = Exercise(file_ex)
