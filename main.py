import argparse
import os
from PIL import Image

def customize(image_path, output_path, fill, padding):
    padding_top = padding
    file_name = os.path.basename(image_path).split(".")[0]
    output_path = image_path + "-folder.png" if output_path == None else output_path + file_name + "-folder.png"
    image = Image.open(image_path).convert("RGBA")
    base_image = Image.open("/Users/phlo/Developer/Scripts/custom-folder/assets/default-folder.png").convert("RGBA")
    
    # Define new image size due to padding, maintaining its aspect ratio
    width = base_image.width - 5*(padding_top*2)
    height = int((image.height / image.width) * width)

    image = image.resize((width, height))
    
    # Change image color to "folder blue"
    if fill:
        data = [(0, 129, 202, a) if a != 0 else (r, g, b, a) for r, g, b, a in image.getdata()]
    else:
        data = [(0, 129, b if a == 0 else 202, a) for a, b, g, r in image.getdata()]
    image.putdata(data)
    
    
    # Calculate coordinates to center image
    width_diff = base_image.width - image.width
    height_diff = base_image.height - image.height
    position = (width_diff // 2, (height_diff // 2 + padding_top))

    # Superimpose the image onto the base image
    base_image.paste(image, position, image)
    
    base_image.save(output_path, "PNG")
    
def valid_file(path):
    if os.path.isfile(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f" {path} does not exist.")
    
def valid_dir(path):
    dir_path = os.path.dirname(path)
    if os.path.isdir(dir_path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"Directory {path} does not exist.")

def main():
    parser = argparse.ArgumentParser(description="Create custom folder image.")
    parser.add_argument("image_path", type=valid_file, help="The path to the png image.")
    parser.add_argument("-o", "--output", type=valid_dir, default=None, help="Optional output path (default is image_path).")
    parser.add_argument("-f", "--fill", action="store_true", help="Optional color fill parameter. If false, the folder color will only be applied as \"highlight\"")
    parser.add_argument("-p", "--padding", type=int, default=45, help="Optional image padding parameter (default is 45).")
    
    args = parser.parse_args()
    
    customize(args.image_path, args.output, args.fill, args.padding)

if __name__ == "__main__":
    main()