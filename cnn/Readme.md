# Remarks
* The classifier assumes that taught caffe model resides in *./model*
directory and is named as *trained_classifier.caffemodel*
* The classifier assumes that mean image in form of numpy array resides
in */model* directory and is named as *model/mean_image.npy*
* Skimage will probably yield a warning. The warning has been suspended in
      the following pull:
      https://github.com/BVLC/caffe/pull/5547/commits/499d60aa250eb9507ed901046d678492c654e3ea
      Nevertheless, in the authors setup '-W ignore' must be also called
      in order to keep output clear.
# Usage
Just call:
```
python -W ignore classify.py [path_to_jpg]
```

.. or the following in case one wants a verbose mode
```
python -W ignore classify.py [path_to_jpg] -v
```
