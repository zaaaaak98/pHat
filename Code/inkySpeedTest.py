import os
import re
import subprocess
import time
from inky import InkyPHAT

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne

font = ImageFont.truetype(FredokaOne, 17)

response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read()

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping[0] = ping[0].replace(',', '.')
download[0] = download[0].replace(',', '.')
upload[0] = upload[0].replace(',', '.')

try:
    if os.stat('/home/pi/speedtest/speedtest.csv').st_size == 0:
        print(Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s))
except:
    pass

print({},{},{},{},{}.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping[0], download[0], upload[0]))

message = "ping " + str(ping[0])
message1 = "download " + str(download[0])
message2 = "upload " + str(upload[0])

x = 10
y = 5

draw.text((x, y), message, inky_display.RED, font)

y = 30

draw.text((x, y), message1, inky_display.BLACK, font)

y = 60

draw.text((x, y), message2, inky_display.RED, font)

inky_display.set_image(img)
inky_display.show()