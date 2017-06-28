#!/usr/bin/env python
"""Dispose any non-jpgs and damaged files from a directory.

Usage:
python discard_non_jpgs.py [directory_to_sieve]

"""

import argparse
from PIL import Image
import os.path
from os import listdir
from os.path import isfile, join

# ------------------------------------------------------------------------------
# Parse the arguments
# ------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("dir_to_sieve", help="Directory to convert.", type=str)
args = parser.parse_args()
print 'Directory to sieve:', args.dir_to_sieve

# ------------------------------------------------------------------------------
# Get list of files
# ------------------------------------------------------------------------------
files_to_check = [os.path.abspath(args.dir_to_sieve + '/' + f)
                  for f in listdir(args.dir_to_sieve)
                  if isfile(join(args.dir_to_sieve, f))]

# ------------------------------------------------------------------------------
# Perform disposal
# ------------------------------------------------------------------------------
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

print 'Finished'