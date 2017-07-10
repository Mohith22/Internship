import Image
import cv2
from pytesseract import image_to_string

img = cv2.imread('sam.jpg')

#print img.shape

c = 0
j=0
ind =-1
Date = " "
Invoice = " "
records = []
for i in range(12):

	if Date==" " or Invoice == " ":
		k = c+200
		img2 = img[c:k,0:img.shape[1]]
	#print img2.shape
	#cv2.imshow('sam',img2)
	#cv2.waitKey(0)
		c = k+12
		res = cv2.resize(img2,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
		cv2.imwrite('new.png',res)
	#print res.shape
		img2 = Image.open('new.png')
		records.append(image_to_string(img2))
		rec = image_to_string(img2)
		print rec
		date = "Date"
		invoice = "Invoice"
		if date in rec:
			ind = rec.index(date)
		if ind!=-1:
			Date = rec[ind+6:ind+16]
		ind = -1
		if invoice in rec:
			ind = rec.index(invoice)
		if ind!=-1:
			Invoice = rec[ind+9:ind+24]

Date = Date.replace(" ","")
Invoice = Invoice.replace(" ","")

print "Date : " + Date
print "Invoice : " + Invoice

