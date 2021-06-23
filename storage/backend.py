import random
from io import BytesIO

from PIL import Image, ImageDraw



def generate_sequence():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = 11
    uid = ''
    while length > 0:
        length -= 1
        uid += chars[random.randint(0, 61)]
    return uid


def get_image(text):
    out = Image.new("RGBA", (150, 100), (255, 255, 255, 0))
    context = ImageDraw.Draw(out)
    context.text((10, 10), text, fill=(255, 255, 255, 255))
    byte_io = BytesIO()
    out.show()
    pic = out.save(byte_io, 'PNG')
    return pic
