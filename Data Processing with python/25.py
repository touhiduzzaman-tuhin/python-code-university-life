import os

import glob

import pandas

def addField(indir = "F:\CODE\Python\Data processing with python"):

    os.chdir(indir)

    filelist = glob.glob('*')

    for filename in filelist:

        df = pandas.read_csv(filename, sep='\s+', header=None)

        df['Station'] = [filename.rsplit("-", 1)[0]] * df.shape[0]

        df.to_csv(filename+".csv", index=None, header=None)

addField()