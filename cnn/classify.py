#!/usr/bin/env python
"""Provides means for classification of supplied image as triangle or circle.

Following script takes path to an image and (optionally) verbosity flag.
The former will checked with ./model/trained_classifier.caffemodel for depicting
either circle or triangle. The probability of each case will be displayed.
Verbosity by default is off. Turning it on will result in printing information
about the cnn initialization from Caffe library.

How to use it with verbose mode:
python -W ignore classify.py [path_to_jpg_file] -v

How to use it with silent mode:
python -W ignore  classify.py [path_to_jpg_file] -v

NOTE: skimage will probably yield a warning. The warning has been suspended in
      the following pull:
      https://github.com/BVLC/caffe/pull/5547/commits/
      499d60aa250eb9507ed901046d678492c654e3ea
      Nevertheless, in the authors setup '-W ignore' must be also called
      in order to keep output clear.

Example of the result:
------------- Classification Results -------------
Triangle:  0.0000168
Circle:    0.9999832

Meaning that provided image is in ~99\% triangle and there is ~1\% chance that
it represents a circle. In other words first entry represents a probability
of the image being triangle, while the second one probability of being a circle.

Please use -h or --help flag in case of any doubts. In particular:
python classify.py -h
python classify.py --help

"""

import sys
import os
import argparse
import numpy as np

# ------------------------------------------------------------------------------
# Parse the arguments
# ------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("image_path", help="Path to an image to classify.", type=str)
parser.add_argument("-v", help="If true, Caffe logs will be displayed. Otherwise, only informations relevant from the point of view of classification process", action='store_false')
args = parser.parse_args()
print '-------------       Data Loaded      -------------'
print 'Image:  ', args.image_path
print 'Verbose:', not args.v, '\n'

if args.v:
    os.environ["GLOG_minloglevel"] = "2"
import caffe

# ------------------------------------------------------------------------------
# Caffe Files Paths
# ------------------------------------------------------------------------------
cnn_net_layers = 'model/deploy.prototxt'
cnn_trained_net = 'model/trained_classifier.caffemodel'
cnn_mean_image = 'model/mean_image.npy'

# ------------------------------------------------------------------------------
# Load the Net
# ------------------------------------------------------------------------------
net = caffe.Net(cnn_net_layers,cnn_trained_net , caffe.TEST)

# ------------------------------------------------------------------------------
# Adapt Data Layer For Input (forced by deploy.prototxt setup)
# ------------------------------------------------------------------------------
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', np.load(cnn_mean_image).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0)) # if using RGB instead of BGR
transformer.set_raw_scale('data', 255.0)
net.blobs['data'].reshape(1,3,227,227)

# ------------------------------------------------------------------------------
# Load Provided Image to The Data Layer
# ------------------------------------------------------------------------------
img = caffe.io.load_image(sys.argv[1])
net.blobs['data'].data[...] = transformer.preprocess('data', img)

# ------------------------------------------------------------------------------
# Classify the Image
# ------------------------------------------------------------------------------
output = net.forward()
print '------------- Classification Results -------------'
print 'Triangle:', "{:10.7f}".format(output['prob'][0][0])
print 'Circle:  ', "{:10.7f}".format(output['prob'][0][1]), '\n'
