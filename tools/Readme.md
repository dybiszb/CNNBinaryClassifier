## Remarks
* Please note that all commands and assumed to be call from the level
of the Readme.md file.
* the scripts are still rather
fragile in terms of OS-related operations as creating non-existing
directories, overwriting files etc, as they were developed only to
speed up the development process. They are definately not suited for
wider community and general purposes.

## Binary Labeling: test_files.txt train_files.txt
Since ../Training/data/train_files.txt and ../Training/data_test_diles.txt are adapted to the author's setup one wants to change their content to fit local development environment. In order to do so simply create_binary_labels
```
python create_binary_labels.py triangles circles ../training/data/
```

##  Convert mean image
Following command will adapt mean_image.binaryproto for loading to python script via converting it to a numpy array (.npy) file. Please note that the command is follows the author's development environment structure and must be slightly change in order to fit one's directories.
```
python convert_meanproto_to_npy.py ../training/data/mean_image.binaryproto ../cnn/model/mean_image.npy
```
## Download URL List
In order to acquire training and testing data of 2 classes the author
helped himself with ImageNet webpage that stores enormous amount of
images sorted according to tags. Obviously for the purpose of
traingle-circle classification set of images depicting the primitives
were needed. Unfortunately, (as far as the author can understand the
webpage) ImageNet only shares list of URLs with the images, hence the
need for the following script.
Files *../ImageNetURLs/triangles_urls.txt* and *../ImageNetURLs/circle
s_urls.txt* contains relevant URLs for the data to be acquired. In order
to download the triangles images to appropriate folder in the author's
setup please call
```
python download_url_list.py ../imageNetURLs/triangles_urls.txt ../training/data/triangles
```
The corresponding command for the circles is as follows
```
python download_url_list.py ../imageNetURLs/circles_urls.txt ../training/data/circles
```
The script will inform how many images were downloaded and how many of them generated errors. The socket timeout is quick (5s), because one can allow himself/herself to skip big files and not working URLs.

## Delete Non-JPGs
Since (as far as the authors knows) Caffe accepts only jpgs (or at least only they do not require additional preprocessing of channels etc.) and the URLs provided by ImageNet not always point to correct images, the author decided to delete corrupted and non-jpg files. Calling the following command will clear the downloaded triangles
```
python discard_non_jpgs.py ../training/data/triangles
```
and corresponding command for circles

```
python discard_non_jpgs.py ../training/data/circles
```
Once again the commands assume the author's directories structure and can be adapted in a straight-forward manner.
