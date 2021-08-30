# pip insatll qrcode
import qrcode
# could be a url or a ticket or anything used these days
data = ''

qr= qrcode.QRcode(version = 1 , box_size= 10 , border=5)
qr.add_data(data)

qr.make(fil=True)

img= qr.make_image(fill_color= 'red', back_color= 'white')
# choose a dir to save the imgae of the qrcode 
img.save()

# decode qrcode
# pip install pyzbar
# pip install pillow
from pyzbar.pyzbar import decode 
# choose the path 
img = Image.open()

r= decode(img)

print(r)