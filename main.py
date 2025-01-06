from reportlab.pdfgen import canvas


FILENAME = "123RatWorksheet.pdf"


def draw_page_xy(worksheet):
    for i in range(0, 11):
        worksheet.drawString(i * 100, 0, f"x={i*100}")
        worksheet.drawString(0, i * 100, f"y={i*100}")


def main():
    worksheet = canvas.Canvas(FILENAME)
    draw_page_xy(worksheet)
    worksheet.save()


if __name__ == "__main__":
    main()
