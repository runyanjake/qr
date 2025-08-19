import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from qrcode.constants import ERROR_CORRECT_H

data_to_encode = "https://linktr.ee/jakerunyanphotography"
image_path = "input/photo.jpeg"

qr = qrcode.QRCode(
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=2
)

qr.add_data(data_to_encode)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=GappedSquareModuleDrawer(),
    embeded_image_path=image_path
)

output_filename = "output/output_qr.svg"
img.save(output_filename)

print(f"Successfully created QR code '{output_filename}' with '{image_path}' embedded.")
