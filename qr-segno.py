import argparse
from pathlib import Path
import segno

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code using segno.")
    parser.add_argument("--data", required=True, help="Data to encode in the QR code")
    parser.add_argument("--output", default="output/output.png", help="Output file path")

    parser.add_argument("--error", choices=['L', 'M', 'Q', 'H'], default='H', help="Error correction level")
    parser.add_argument("--version", type=int, help="Version of the QR code (1-40). Leave empty for auto")
    parser.add_argument("--micro", action="store_true", help="Generate a Micro QR code if possible")
    parser.add_argument("--mask", type=int, choices=range(8), help="Mask pattern (0-7). Leave empty for automatic")
    parser.add_argument("--scale", type=int, default=10, help="Module size (scale)")
    parser.add_argument("--border", type=int, default=4, help="Border size in modules")
    parser.add_argument("--dark", default="000000", help="Hexcode (without #) for color of the dark modules")
    parser.add_argument("--light", default="ffffff", help="Hexcode (without #) for color of the light modules")

    args = parser.parse_args()

    make_kwargs = {"error": args.error}
    if args.version is not None:
        make_kwargs["version"] = args.version
    if args.micro:
        make_kwargs["micro"] = True
    if args.mask is not None:
        make_kwargs["mask"] = args.mask

    qr = segno.make(args.data, **make_kwargs)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    ext = Path(args.output).suffix.lower()[1:]

    save_kwargs = {
        "scale": args.scale,
        "border": args.border,
        "dark": "#" + args.dark,
        "light": "#" + args.light,
        "kind": ext,
    }
    qr.save(args.output, **save_kwargs)

    print(f"✅ QR code saved to '{args.output}' "
          f"(error={args.error}, version={args.version}, micro={args.micro}, mask={args.mask}, "
          f"scale={args.scale}, border={args.border}, kind={ext})")

if __name__ == "__main__":
    main()

