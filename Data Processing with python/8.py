import patoolib

import os

os.chdir("F:\CODE\Python\Data processing with python")


patoolib.extract_archive("test.gz", outdir="test")

os.listdir("test")

