import argparse
from PIL import Image
import os, os.path
from os import listdir
from os.path import isfile, join
import imghdr

parser = argparse.ArgumentParser()
parser.add_argument("dir_to_convert", help="Directory to convert.", type=str)
args = parser.parse_args()
print '[-] Directory to convert:', args.dir_to_convert

files_to_check = [os.path.abspath(args.dir_to_convert + '/' + f) for f in listdir(args.dir_to_convert) if isfile(join(args.dir_to_convert, f))]

for f in files_to_check:
    pre, ext = os.path.splitext(f)
    if ext.lower() == ".jpg":
        try:
            im = Image.open(f)
            if not im.format == 'JPEG':
                raise
            im.verify()
        except Exception, e:
            os.remove(f)
    else:
        os.remove(f)
