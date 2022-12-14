from os import chdir
from pathlib import Path

# see: https://zetcode.com/python/pathlib/

def main() -> None:
    # current working directory and home directory
    cwd = Path.cwd()
    home = Path.home()
    print(f"\nCurrent working directory: {cwd}", end="\n")
    print(f"Home directory: {home}", end="\n")
    print(f"path Parent: {home.resolve().parent}")

    currfile = Path(__file__)
    print(f"Current file path: {currfile}", end="\n")

    parentpath = Path(__file__).parent
    print(f"parentpath: {parentpath}", end="\n")

    im_dir = parentpath / "Images"
    print(f"im_dir_path: {im_dir}", end="\n")

    relative = currfile.relative_to(cwd)
    print(f"relative file: {relative}", end="\n\n")

    # im_dir = "docs/turtle"
    # cwd = Path.cwd()
    # im_fp = cwd / im_dir
    # files = [f for f in im_fp.iterdir() if f.is_file()]
    # im2_files = [f for f in im_fp.iterdir() if f.suffix == '.png']  # suffix
    # files_rel = [sfile.relative_to(cwd) for sfile in files]
    # for i in files_rel:
    #     print(f'"{i}"', end=", ")
    # print("\n\n")
    # im2_files = [sfile.relative_to(cwd) for sfile in im2_files]
    # for i in files_rel:
    #     print(f'"{i}"', end=", ")

'''
    # creating paths
    path = Path("/usr/bin/python3")
    print(path)

    # using backslashes on Windows
    path = Path(r"C:\Windows\System32\cmd.exe")
    print(path)

    # using forward slash operator
    path = Path("/usr") / "bin" / "python3"
    print(path)

    # using joinpath
    path = Path("/usr").joinpath("bin", "python3")
    print(path)

    # reading a file from a path
    # path = Path.cwd() / "settings.yaml"
    # with path.open() as file:
    #     print(file.read())

    # reading a file from a path using read_text
    # print(path.read_text())

    # resolving a path
    path = Path("settings.yaml")
    full_path = path.resolve()
    print(f"Path resolve: {full_path}")

    # path member variables
    print(f"Path: {full_path}")
    print(f"Parent: {full_path.parent}")
    print(f"Grandparent: {full_path.parent.parent}")
    print(f"Name: {full_path.name}")
    print(f"Stem: {full_path.stem}")
    print(f"Suffix: {full_path.suffix}")

    # testing whether a path is a directory or a file
    print(f"Is directory: {full_path.is_dir()}")
    print(f"Is file: {full_path.is_file()}")

    # testing whether a path exists
    print(f"Full path exists: {full_path.exists()}")
    wrong_path = Path("/usr/does/not/exist")
    print(f"Wrong path exists: {wrong_path.exists()}")

    # creating a file
    new_file = Path.cwd() / "new_file.txt"
    new_file.touch()

    # writing to a file
    new_file.write_text("Hello World!")

    # deleting a file
    # new_file.unlink()

    # creating a directory
    new_dir = Path.cwd() / "new_dir"
    if new_dir.exists():
        print(f"exists: {new_dir}")
    else:
        new_dir.mkdir()
        print(f"created: {new_dir}")

    # changing to the new directory
    chdir(new_dir)
    print(f"Current working directory: {Path.cwd()}")

    # deleting a directory
    # new_dir.rmdir()
'''

if __name__ == "__main__":
    main()