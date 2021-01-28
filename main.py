#Simple QR code decoder using opencv and pyzbar
import cv2
from pyzbar.pyzbar import decode


#membaca file image agar bisa di terjemahkan oleh program
img = cv2.imread('qr.jpg')

#Looping for untuk print data dan type code yang telah di decode
for code in decode(img) :
    print(code.type)
    #Agar output hanya berisikan data dari QR Code nya saja
    print(code.data.decode('utf-8'))
