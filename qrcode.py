import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.constants import ERROR_CORRECT_H, ERROR_CORRECT_Q, ERROR_CORRECT_M, ERROR_CORRECT_L

data_to_encode = "https://linktr.ee/jakerunyanphotography"
input_image_path = "input/photo.jpeg"
output_image_path = "output/output.png"

qr = qrcode.QRCode(
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=1
)

qr.add_data(data_to_encode)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=SquareModuleDrawer(),
    embeded_image_path=input_image_path
)

img.save(output_image_path)

print(f"Successfully created QR code '{output_image_path}' with '{input_image_path}' embedded.")
