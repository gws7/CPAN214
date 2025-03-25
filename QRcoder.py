import qrcode

# Data to be encoded
data = "https://www.linkedin.com/in/gabriel-w-sosin-a5061b1bb/"

# Creating a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR grid
    border=0,  # Border size around the QR Code
)

# Adding data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Creating an image of the QR code
qr_image = qr.make_image(fill="black", back_color="white")

# Save the QR code image
qr_image.save("LinkedIn.png")

# Show the QR code image
qr_image.show()