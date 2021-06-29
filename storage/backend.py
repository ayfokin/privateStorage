import random
from datetime import datetime
import pytz

from background_task import background

from storage.models import Data

from PIL import Image, ImageDraw, ImageFont


def generate_sequence():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = 11
    uid = ''
    while length > 0:
        length -= 1
        uid += chars[random.randint(0, 61)]
    return uid


def create_image(text, file):
    out = Image.new("RGB", (1, 1), color='#222226')
    context = ImageDraw.Draw(out)
    font = ImageFont.truetype('/media/fonts/verdana.ttf', size=18)
    out = out.resize(i + 14 for i in context.textsize(text, font))
    context = ImageDraw.Draw(out)
    context.text((7, 3), text, (245, 245, 245), font=font)
    out.save(file, "PNG")


@background()
def optimize_db():
    now = pytz.utc.localize(datetime.utcnow())
    for i in Data.Entry.all():
        if (now - i.create_time).days >= 7:
            i.delete()
