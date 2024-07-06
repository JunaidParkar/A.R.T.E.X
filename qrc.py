from PIL import Image
from pyzbar import pyzbar

img = Image.open('qr.png')
output = pyzbar.decode(img)
print(output)