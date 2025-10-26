import pywhatkit
from images_code import main_img, path
import datetime

t = datetime.datetime.now()
h: int = int(t.strftime('%H'))
m: int = int(t.strftime('%M')) + 1
print(t, h, m)


whatsapp_group_id = 'Your id'
caption = ''



if h >= 18:
    caption = "Market Close!"
else:
    caption = "Market Open!"

try:
    pywhatkit.sendwhats_image(whatsapp_group_id, path , caption, h, m)
except:
    print("failed to send summary")