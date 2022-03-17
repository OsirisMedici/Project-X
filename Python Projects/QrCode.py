from textwrap import fill
import qrcode
import image
qr =qrcode.QRCode(
    version=15,
    box_size=10,
    border=5,
)
data = input("Enter the Link :- ")

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color ="white")
nme = input("Enter the fukinn name you want to save QR code.. ex-name.png: ")
img = img.save(nme)
