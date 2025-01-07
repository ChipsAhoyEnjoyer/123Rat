import worksheet


FILENAME = "123RatWorksheet.pdf"


def main():
    pdf = worksheet.Worksheet(FILENAME)
    pdf.draw_page_xy_ruler()
    pdf.generate_pdf()


if __name__ == "__main__":
    main()
