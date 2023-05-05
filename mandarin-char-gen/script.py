from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os


def create_pdf(character, file_name):
    c = canvas.Canvas(file_name, pagesize=A4)
    pdfmetrics.registerFont(TTFont('Heiti', '/System/Library/Fonts/STHeiti Light.ttc'))
    c.setFont('Heiti', 300)
    width, height = A4

    # Get the size of the character
    char_width = c.stringWidth(character, 'Heiti', 300)

    # Calculate the position to center the character
    x_pos = (width - char_width) / 2
    y_pos = (height - 100) / 2

    # Draw the character on the canvas
    c.drawString(x_pos, y_pos, character)
    c.showPage()
    c.save()


def read_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        characters = [line.strip() for line in file]
    return characters


def main():
    # List of characters
    list_location = 'common3500.txt'
    characters = read_characters(list_location)

    # Generate a PDF for each character
    for idx, char in enumerate(characters):
        file_name = f'output/character_{idx + 1}.pdf'
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        create_pdf(char, file_name)
        print(f"Generated PDF for '{char}' as '{file_name}'")


if __name__ == '__main__':
    main()
