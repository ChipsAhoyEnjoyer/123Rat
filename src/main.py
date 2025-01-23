import worksheet
import exercises


FILENAME = "123RatWorksheet.pdf"
VALID_SHAPES = exercises.SHAPES


def main():
    print("Welcome to 123Rat! This name is definitely not an ABCMouse parody....")
    trace1 = input("What word would you like to practice tracing? Leave blank to generate random word.\n")
    trace2 = input("How about one more word? Again, leave blank to generate random word.\n")
    while True:
        shape = input(
            f"Here are some shapes: {' / '.join(VALID_SHAPES)}\n"
            f"Choose a shape to color? Leave blank to choose randomly.\n"
        )
        if shape.lower() in VALID_SHAPES or shape == "":
            break
        print("Invalid shape, try again...")
    print("Generating worksheet!")
    empty_sheet = worksheet.Worksheet(FILENAME)
    exercise1 = exercises.LetterTraceExercise(empty_sheet, trace1)
    exercise2 = exercises.LetterTraceExercise(exercise1, trace2)
    exercise3 = exercises.ColorShapeExercise(exercise2, shape)
    exercise3.generate_exercises()
    print(f"Done. Open the {FILENAME} file in the program's src folder to print the results.")


if __name__ == "__main__":
    main()

# TODO: add a max cap to exercises i.e. Max length for words in the Letter trace exercise,
#       max shapes for Color Shape exercise
# TODO: add Tkinter UI
# TODO: make logo prettier
# TODO: add os paths to better control where the generated file lands