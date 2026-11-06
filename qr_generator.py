import qrcode

url = input("Enter the URL to generate QR code: ")
filename = input("Enter the filename to save the QR code: ")
filepath = input("Enter the file path to save the QR code: (LEAVE EMPTY IF YOUR AMMAR) ")

if filepath == "":
 filepath = "C:\\Users\\ammar\\OneDrive\\Desktop\\QR CODES\\{filename}.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filepath.format(filename=filename))

print("QR code generated and saved successfully at: {}".format(filepath.format(filename=filename)))