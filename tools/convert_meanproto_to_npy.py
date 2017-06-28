# https://github.com/BVLC/caffe/issues/290
# user: sg90

import caffe
import numpy as np
import sys

if len(sys.argv) != 3:
    print "Usage: python convert_protobuff_to_npy.py mean.binaryproto out.npy"
    sys.exit()

try:
    blob = caffe.proto.caffe_pb2.BlobProto()
    data = open( sys.argv[1] , 'rb' ).read()
    blob.ParseFromString(data)
    arr = np.array( caffe.io.blobproto_to_array(blob) )
    out = arr[0]
    np.save( sys.argv[2] , out )
except Exception, e:
    print 'Error', e
