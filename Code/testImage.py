from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
import requests
import tempfile
import shutil

url = "https://raw.githubusercontent.com/zaaaaak98/pHat/master/testImage.png"

res = requests.get(url, stream=True)

temp = tempfile.TemporaryFile()
res.raw.decode_content=True
shutil.copyfileobj(res.raw, temp)
del res

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)
img = Image.open(temp)

inky_display.set_image(img)
inky_display.show()