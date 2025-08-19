import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.constants import ERROR_CORRECT_H

data_to_encode = "https://linktr.ee/jakerunyanphotography"
image_path = "data/photo.jpeg"

qr = qrcode.QRCode(
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(data_to_encode)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path=image_path
)

output_filename = "data/qr_with_logo.png"
img.save(output_filename)

print(f"Successfully created QR code '{output_filename}' with '{image_path}' embedded.")