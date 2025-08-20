import argparse 
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, RoundedModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.constants import ERROR_CORRECT_H, ERROR_CORRECT_Q, ERROR_CORRECT_M, ERROR_CORRECT_L

output_image_path = "output/output.png"

DRAWER_MAP = {
    "SquareModuleDrawer": SquareModuleDrawer,
    "GappedSquareModuleDrawer": GappedSquareModuleDrawer,
    "CircleModuleDrawer": CircleModuleDrawer,
    "RoundedModuleDrawer": RoundedModuleDrawer,
    "VerticalBarsDrawer": VerticalBarsDrawer,
    "HorizontalBarsDrawer": HorizontalBarsDrawer,
}

CORRECTION_MAP = {
    "ERROR_CORRECT_L": ERROR_CORRECT_L,
    "ERROR_CORRECT_M": ERROR_CORRECT_M,
    "ERROR_CORRECT_Q": ERROR_CORRECT_Q,
    "ERROR_CORRECT_H": ERROR_CORRECT_H,
}

def main():
    parser = argparse.ArgumentParser(description="Generate a styled QR code with qrcode.")
    parser.add_argument("--drawer", choices=DRAWER_MAP.keys(), default="SquareModuleDrawer", help="Module drawer style")
    parser.add_argument("--correction", choices=CORRECTION_MAP.keys(), default="ERROR_CORRECT_H", help="Error correction level")
    parser.add_argument("--data", required=True, help="Data to encode in the QR code")
    parser.add_argument("--input-image", help="Path to the image to embed")
    parser.add_argument("--output", default="output/output.png", help="Output file path")

    args = parser.parse_args()

    drawer_class = DRAWER_MAP[args.drawer]
    correction_level = CORRECTION_MAP[args.correction]

    qr = qrcode.QRCode(
        error_correction=correction_level,
        box_size=10,
        border=1,
    )

    qr.add_data(args.data)
    qr.make(fit=True)

    print("args.input_image: " + str(args.input_image))

    if args.input_image is not None:
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=drawer_class(),
            embeded_image_path=args.input_image,
        )
    else:
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=drawer_class(),
        )

    img.save(args.output)

    print(f"✅ Successfully created QR code '{args.output}' with '{args.input_image}' embedded "
          f"(drawer={args.drawer}, correction={args.correction})")

if __name__ == "__main__":
    main()
