from PIL import Image
import argparse
from pathlib import Path
from .simulation import LedMatrixPreview

class ArgsNamespace(argparse.Namespace):
    image_path : Path
    size : tuple[int, int]
    
    preview : bool
    circle_pixel : bool
    led_size : int
    margin : int


def create_parser(tool_name):
    parser = argparse.ArgumentParser(description=tool_name, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # Positional arguments
    parser.add_argument("image_path", type=Path, help="Path to the image file.")

    # Optional arguments
    parser.add_argument("-s","--size", type=int, nargs=2, default=(16, 16), help="Size of the LED matrix as width height.")

    # Preview options
    parser.add_argument("-p","--preview", action="store_true", help="Preview the image on an LED matrix.")
    parser.add_argument("-l","--led_size", type=int, default=30, help="Size of each LED in pixels.")
    parser.add_argument("-m","--margin", type=int, default=2, help="Margin between LEDs in pixels.")
    parser.add_argument("-c","--circle_pixel", action="store_true", help="Use circular LEDs instead of square ones.")
    return parser.parse_args(namespace=ArgsNamespace())

def main():
    args = create_parser("LED Matrix Image Converter")
    print(f"Arguments: {vars(args)}")

    # === CONFIG ===
    IMAGE_PATH = args.image_path.absolute()
    MATRIX_SIZE = args.size
    LED_SIZE = args.led_size
    MARGIN = args.margin
    CIRCLE = args.circle_pixel

    # === LOAD IMAGE ===
    image = Image.open(IMAGE_PATH).convert("RGB")
    image = image.resize(MATRIX_SIZE, Image.LANCZOS)
    pixels = image.load()

    with open(IMAGE_PATH.with_suffix(".rgb"), "w") as f:
        for y in range(MATRIX_SIZE[1]):
            for x in range(MATRIX_SIZE[0]):
                color = pixels[x, y]
                f.write(f"{color[0]} {color[1]} {color[2]}\n")

    if args.preview:
        preview = LedMatrixPreview(pixels, MATRIX_SIZE, IMAGE_PATH, LED_SIZE, MARGIN, CIRCLE)
        preview.run()

if __name__ == "__main__":
    main()
