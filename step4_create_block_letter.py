import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_block_letter_s(height: int, width: int, letter: str = "S", font_size_ratio: float = 0.9) -> np.ndarray:
    img = Image.new('L', (width, height), color=255)
    draw = ImageDraw.Draw(img)
    font_size = int(min(height, width) * font_size_ratio)
    font = None
    font_paths = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in font_paths:
        try:
            font = ImageFont.truetype(path, font_size)
            break
        except:
            continue
    if font is None:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), letter, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2 - bbox[0]
    y = (height - text_height) // 2 - bbox[1]
    draw.text((x, y), letter, fill=0, font=font)
    arr = np.array(img, dtype=np.float64) / 255.0
    return arr
    