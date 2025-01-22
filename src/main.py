import worksheet


FILENAME = "123RatWorksheet.pdf"


def main():
    pdf = worksheet.Worksheet(FILENAME)
    pdf.generate_pdf()


if __name__ == "__main__":
    main()

# TODO: add a max cap to exercises i.e. Max length for words in the Letter trace exercise,
#       max shapes for Color Shape exercise
# TODO: add Tkinter UI
# TODO: make logo prettier