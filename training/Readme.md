## Remarks
* All commands and assumed to be call from the level of the
Readme.md.

* Training net_lmdb.prototxt on the author's machine does not work.
It is to be (hopefully) fixed in the future. Something is wrong
with 'epoch procedure' and batches cannot be loaded properly to
the Caffe. Training net_hdf5.prototxt works normally.

## HLF5 Data Labeling
Please note that data/train_files.txt and data/test_files.txt are adapted to the author's setup. The repository was intended to help the author's developmnet process, hence full generality is not acquired. In order to change it please refer to ../Tools/Readme.md and its Labeling section. It will overwrite the paths in relevant files on the fly.

## LMDB Creation
In case when one wants to create new lm data base from (perhaps)
his/her custom set of training/testing images, the following
steps are more than advised.

Create LMDB data base from TRAIN files:
```
GLOG_logtosderr=1 [path_to_caffe]/build/tools/convert_imageset --resize_height=256 --resize_width=256 --shuffle / data/train_files.txt data/train_lmdb
```

Create LMDB data base from TEST files:
```
GLOG_logtosderr=1 [path_to_caffe]/build/tools/convert_imageset --resize_height=256 --resize_width=256 --shuffle / data/test_files.txt data/test_lmdb
```

## Mean Image
It is assumed that mean_image.binaryproto will be converted to
mean_image.npy and shipped with the taught cnn.
The .npy file already resides in ../cnn/model/ directory but
in case one wants to adapt it to its custom lmdb here is
the command
```
[path_to_caffe]/build/tools/compute_image_mean data/train_lmdb data/mean_image.binaryproto
```

## Training
There two options for supplying the data to the network,
hence there are two definitions of the network: net_lmdb.prototxt
 and net_hdf5.prototxt. The former assumes that training and
 testing images are loaded from lmdb data base, while the latter
 loads the images to the memory without any sophisticated
 operations. The images are loaded based on data/train_files.txt
 and data/test_files.txt. Please note that the hdf5 solution
 must be adapted to one's machine's memory capacity. It can be
 simply done via modifying 'batch_size' property of TRAIN and
 TEST ImageData layers in net_hdf5.prototxt file. To train the
  network via lmdb approach just call
```
[path_to_caffe]/build/tools/caffe train --solver solver_lmdb.prototxt
```
or, for hdf5 solution, call
```
[path_to_caffe]/build/tools/caffe train --solver solver_hdf5.prototxt
```
Calling one of the above will produce train_iter_10000.caffemodel
 and train_iter_10000.solverstate files in the current
 directory. The latter can be deleted as it is only a caching
 mechanism for Caffe. The former on the other hand constitute a
  CNN learned to distinguish triangles from circles (or any other
   custom binary classification if one did change training and
   testing set of images). The network itself is unfortunately
   not enough to classify arbitrary image. For further
   instructions please refer to ../cnn/Readme.md.

## Visualizing Network
Caffe comes with simple tool for visualiz convolutional net
 defined in .prototxt file. In order to visualize the net call
```
[path_to_caffe]/python/draw_net.py net_hdf5.prototxt ../cnn/model/net_visualization.png
```

Since net_hdf5.prototxt and net_lmdb.prototxt have the same structure, the above command can be called with either of them. Again, output structure follows the author's directories setup.
