from PIL import Image
from pathlib import Path
import glob
from math import ceil, floor


def create_collage(
    images_per_row, img_width, img_height, padding, images, savefilepath
):
    frame_width = (img_width * images_per_row) + (padding * (images_per_row - 1))
    cell_width = ceil((frame_width + padding) / images_per_row)
    new_image_width = cell_width - padding
    scaling_factor = new_image_width / img_width

    scaled_img_width = ceil(img_width * scaling_factor)
    scaled_img_height = ceil(img_height * scaling_factor)

    cell_height = scaled_img_height + padding

    number_of_rows = ceil(len(images) / images_per_row)
    frame_height = cell_height * number_of_rows - padding

    new_im = Image.new("RGB", (frame_width, frame_height))

    x_cord = 0
    for num, im in enumerate(images):
        if num % images_per_row == 0:
            x_cord = 0
        im = Image.open(im)
        im.thumbnail((scaled_img_width, scaled_img_height))
        y_cord = (num // images_per_row) * cell_height
        new_im.paste(im, (x_cord, y_cord))
        x_cord += cell_width
    # using PNG because JPEG is lossy
    new_im.save(savefilepath, "PNG", quality=80, optimize=True, progressive=True)


def save_collage(img_fol, save_rel_path, img_in_row=6):
    workingfolderpath = Path(__file__).parent
    imgfolderpath = Path(__file__).parent / img_fol
    savefilepath = workingfolderpath / save_rel_path
    listofimages = list(imgfolderpath.glob("*.png"))
    width, height = Image.open(
        listofimages[0]
    ).size  # get size of images (assume all same size)
    create_collage(img_in_row, width, height, 10, listofimages, savefilepath)


# save_collage("Spiro_a/", "collages/CollageSpiro_a.png", img_in_row=5)
save_collage("Spiro_b/", "collages/CollageSpiro_b.png", img_in_row=5)
# save_collage("Spiro_d/", "collages/CollageSpiro_d.png", img_in_row=5)
