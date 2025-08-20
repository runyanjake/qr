import argparse
import segno
from PIL import Image

def create_artistic_qr(data, background_path, output_path, scale, error_correction):
    qr = segno.make(data, error=error_correction)

    qr.to_artistic(background=background_path, target=output_path, kind='png', scale=scale)
    print(f"Artistic QR code saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate an artistic QR code with a background image.")
    parser.add_argument('--data', help="The data to encode in the QR code.")
    parser.add_argument('--background', help="Path to the background image.")
    parser.add_argument('--output', help="Path to save the generated QR code image.")
    parser.add_argument('--scale', type=int, default=10, help="Scale factor for the QR code image.")
    parser.add_argument('--error-correction', type=str, choices=['L', 'M', 'Q', 'H'], default='L',
                        help="Error correction level for the QR code.")

    args = parser.parse_args()

    create_artistic_qr(args.data, args.background, args.output, args.scale, args.error_correction)

if __name__ == "__main__":
    main()

