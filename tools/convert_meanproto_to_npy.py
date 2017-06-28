#!/usr/bin/env python
"""Converts .binaryproto into .npy.

The script is useful in case when one wants to convert a mean image created
based on lmdb data base into a numpy array file that is accessible to python
script.

Usage:
python convert_meanproto_to_npy.py [binaryproto_path] [npy_output_path]

NOTE: The script is heavily based on sg90's answer in the following thread:
      https://github.com/BVLC/caffe/issues/290

"""

import numpy as np
import argparse
import caffe

# ------------------------------------------------------------------------------
# Parse the arguments
# ------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("binary_proto_path", help="Path to .binaryproto file.",
                    type=str)
parser.add_argument("npy_output_path", help="Path to resulting .npy file.",
                    type=str)
args = parser.parse_args()
print '-------------       Data Loaded      -------------'
print 'Binaryproto:', args.binary_proto_path
print 'Npy        :', args.npy_output_path

try:
    blob = caffe.proto.caffe_pb2.BlobProto()
    data = open( args.binary_proto_path , 'rb' ).read()
    blob.ParseFromString(data)
    arr = np.array( caffe.io.blobproto_to_array(blob) )
    out = arr[0]
    np.save( args.npy_output_path , out )
except Exception, e:
    print 'Error', e

print 'Finished.'