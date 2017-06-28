#!/usr/bin/env python
"""Downloads files from list oof URLs.

The script is useful in case when one wants to convert a mean image created
based on lmdb data base into a numpy array file that is accessible to python
script. Please note that URLs must be in readable files saved in separate lines.

Usage:
python download_url_list.py [path _to_url_list] [output_directory]

"""
import urllib
import argparse
import sys
import os
import socket

# ------------------------------------------------------------------------------
# Parse the arguments
# ------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("url_list_path", help="Path to a file containing per-line "
                                          "urls to download.", type=str)
parser.add_argument("output_path", help="Path to store downloaded files.",
                    type=str)
args = parser.parse_args()
print '-------------         Setting       -------------'
print 'Loading URLs from:', args.url_list_path
print 'Saving files to  :', args.output_path

# ------------------------------------------------------------------------------
# Download files from URLs
# ------------------------------------------------------------------------------
socket.setdefaulttimeout(5)
num_lines = sum(1 for line in open(args.url_list_path))
i = 1
error_img = 0
with open(args.url_list_path) as f:
    for url in f:
        url = url.rstrip('\n')
        filename = url.split('/')[-1]
        output_path = args.output_path + '/' + filename
        if not os.path.exists(args.output_path):
            os.makedirs(args.output_path)

        try:
            urllib.urlretrieve(url, output_path)
            i=i+1
        except Exception, e:
            # TODO move to other function or remove
            try:
                os.remove(output_path)
            except OSError:
                pass
            error_img = error_img + 1

        sys.stdout.write("\rImages downloaded: %d/%d | "
                         "Error while downloading %d" %
                         (i, num_lines, error_img))
        sys.stdout.flush()

print 'Finished'
