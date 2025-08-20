# QR Codes
Generating my own QR codes.

# Setup 

## Python 
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt 
```

# Examples

## qrcode  
```
python qr-qrcode.py --drawer SquareModuleDrawer --correction ERROR_CORRECT_H --data https://linktr.ee/jakerunyanphotography --input-image ./input/photo.jpeg --output output/output.png
python qr-qrcode.py --drawer SquareModuleDrawer --correction ERROR_CORRECT_H --data https://linktr.ee/jakerunyanphotography --output output/output.png
```

## segno
```
python qr-segno.py --data https://whitney.rip --output examples/segno/embed.png
```

