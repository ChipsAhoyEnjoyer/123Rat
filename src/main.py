import worksheet


FILENAME = "123RatWorksheet.pdf"


def main():
    pdf = worksheet.Worksheet(FILENAME, draw_ruler=True)
    pdf.generate_pdf()


if __name__ == "__main__":
    main()
