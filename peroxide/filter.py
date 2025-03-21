from pathlib import Path
import sys

sys.path.insert(0, str(Path.home() / 'Documents/GitHub/files-1.0.0/files'))
from files import File

from .tools import *
from .startup import *  # Imports the pre-processed command-line arguments
from .program import Program

GRAPHIC_FILE_EXTS = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'svg']

class Filter(Program):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_files(self):
        for file in ARGS.args:
            if not os.path.exists(file):
                print(f"File does not exist: {file}")
                continue

            if os.path.isdir(file):
                if RECURSIVE:
                    for root, _, files in os.walk(file, followlinks=FOLLOW):
                        for f in files:
                            print(os.path.join(root, f))
                else:
                    self.process(file)
            else:
                self.process(file)

    @str2path_method
    def process(self, s):
        log.info(f"Processing {s=}...")

    def run(self):
        self.process_files()

if __name__ == "__main__":
    filter_program = Filter()
    filter_program.process_files()
