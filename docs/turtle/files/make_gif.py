from PIL import Image
from pathlib import Path

dir = Path.cwd()


def make_gif(filesfolder, savefile, duration=100):
    wd = Path(__file__).parent
    imgfolder = wd / filesfolder
    savefile = wd / savefile
    files = imgfolder.glob("*.png")
    frames = [Image.open(image) for image in files]
    # print(frames)
    frame_one = frames[0]
    frame_one.save(
        savefile,
        format="GIF",
        append_images=frames,
        save_all=True,
        duration=duration,
        loop=0,
    )


if __name__ == "__main__":
    # make_gif("Spiro_a/", "gifs/spiro_a.gif")
    make_gif("Spiro_b/", "gifs/spiro_b.gif", duration=200)
    # make_gif("Spiro_d/", "gifs/spiro_d.gif")
