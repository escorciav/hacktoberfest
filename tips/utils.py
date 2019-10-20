import base64
import io
import textwrap
from pathlib import Path

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

IMAGE_SIZE = 300
FONT_SIZE = 20
MARGIN = 40
STRING_WIDTH = 25


def parse_tips(folder='tips'):
    "mid-challenge"
    folder = Path(folder)

    tips = []
    for file in folder.glob('*.md'):
        content = open(file, 'r', encoding='utf-8').read()

        hashtags = []
        for word in content.split(' '):
            if len(word) > 1 and word[0] == '#':
                hashtags.append(word.strip())

        tips.append(
            {
               "hastags": ' '.join(hashtags),
               "tip": content
            }
        )
    return tips


def create_image(message):
    "senior challenge"
    img = Image.new("RGBA", (IMAGE_SIZE, IMAGE_SIZE), "yellow")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)

    lines = [
        line.center(STRING_WIDTH)
        for line in textwrap.wrap(message, width=STRING_WIDTH)
    ]

    offset = MARGIN
    for line in lines:
        w, h = draw.textsize(line, font=font)
        draw.text(
            (MARGIN, offset),
            line,
            fill="red",
            font=font,
        )
        offset += h

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return base64.b64encode(img_byte_arr.getvalue())

if __name__ == '__main__':
    # Super dummy unit-test
    tips = parse_tips(Path('.'))
    image_b64 = create_image(tips[0]['tip'])
    print('Search base64 to image in google ;)')
    print(image_b64.decode())