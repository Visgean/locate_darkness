#!/usr/bin/env python3

from pathlib import Path

import argparse
import shutil
import os

parser = argparse.ArgumentParser(
    description="Locate image file that have already been processed and move them to special directory.")
parser.add_argument('source', help='folder with original files')
parser.add_argument('edited', help='folder with edited files')


# noinspection PyTypeChecker
def main():
    args = parser.parse_args()

    source_folder = Path(args.source).absolute()
    edited_folder = Path(args.edited).absolute()

    destination_folder = (source_folder / 'edited').absolute()
    os.makedirs(destination_folder, exist_ok=True)

    exported_files = []
    for edited_file in edited_folder.glob("dark_*"):
        filename, file_extension = os.path.splitext(edited_file.name.lstrip('dark_'))
        exported_files.append(filename)

    for file in source_folder.iterdir():
        filename, file_extension = os.path.splitext(file.name)
        xmp_file = source_folder / (str(file.name) + '.xmp')

        if filename in exported_files:
            print(filename, 'has been edited')
            shutil.move(str(file.absolute()), str(destination_folder.absolute()))
            if xmp_file.exists():
                shutil.move(str(xmp_file.absolute()), str(destination_folder.absolute()))


if __name__ == '__main__':
    main()
