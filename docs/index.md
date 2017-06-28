## Test Data
In order to obtain the data for training/testing purposes, I helped
myself with ImageNet webpage. The page contains of enormous number
of images, sorted according to tags. Using tags *triangle* and
*circle* I was able to put my hands on the URLs lists and utilizing
simple python script enabled me to download the images and dispose
any that was damaged. There are:
* 153 triangle pictures
* 564 circle pictures

Although there is almost 4 times more pictures of circles I was courious
how the network will response to such disproportion and how it effects
the final classifier, hence I proceeded.

Following table presents the ratio between testing and training sets
in both, circle and triangles images. The rproportion is 9:1 or in other
words: 90% of images in triangles/circles set was used for training and
10% for testing.
<table>
<tr>
    <td></td>
    <td>Training</td>
    <td>Testing</td>
</tr>
<tr>
    <td>Triangle</td>
    <td>137</td>
    <td>16</td>
</tr>
<tr>
    <td>Circle</td>
    <td>507</td>
    <td>57</td>
</tr>
</table>


## Network Design
Since the task purpose was to understand the basics of Caffe framework
and the thesis involvement in designing convolutional neural networks
is rather small, I assumed that it would be ok to use an existing
model of layers. The model is BAIR/BVLC CaffeNet Model with a slight
modification in fully connected *fc8* - instead of 100 classes, 2 were
set. Following image depicts the network layers setup. It has been
produced with *draw_net.py* script shipped with Caffe.

<img src="net_visualization.png" alt="HTML5 Icon">

(Chrome) Please right click on the image and select 'Open image in new
tab'. Then, by clicking on magnifying glass one can inspect fully sized
image.

## Results
Set of results for images depicting triangles that should be obvious for
the classifier to classify. Any change in perspective with a triangle
image results in dramatic change in performance. It is most probably
caused by low number of triangle images provided for training the
classifier and not so many examples with strange camera angles.
<table>
<tr>
    <th>Image</th>
    <td><img src="http://farm2.static.flickr.com/1133/638741937_fb6d083357.jpg?v=0" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm4.static.flickr.com/3622/3362307618_590e37da12.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm6.static.flickr.com/5261/5579646031_c7900ff6c8.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm4.static.flickr.com/3069/2371655967_71722f1848.jpg" alt="HTML5 Icon" width="150" height="150"></td>
</tr>

<tr>
    <th>Triangle</th>
    <td>0.9980729</td>
    <td>0.0000309</td>
    <td>0.9998710</td>
    <td>0.6579151</td>
</tr>

<tr>
    <th>Circle</th>
    <td>0.0019271</td>
    <td>0.9999691</td>
    <td>0.0001289</td>
    <td>0.3420849</td>
</tr>
</table>

<table>
<tr>
    <th>Image</th>
    <td><img src="http://farm1.static.flickr.com/208/467603366_cfc237571e.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm3.static.flickr.com/2436/3949033524_dc688743cc.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://1.bp.blogspot.com/_SO_1-gB06t0/THKKKLGsZdI/AAAAAAAAD0I/EkRvobQicq8/s1600/IMGP8509.JPG" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://www.kelabhk.com/CREATIVEPHOTO/ALLPHOTO/DoubleCONE.jpg" alt="HTML5 Icon" width="150" height="150"></td>
</tr>

<tr>
    <th>Triangle</th>
    <td>0.9999931</td>
    <td>0.9999542</td>
    <td>0.2439452</td>
    <td>0.9409665</td>
</tr>

<tr>
    <th>Circle</th>
    <td>0.0000069</td>
    <td>0.0000458</td>
    <td>0.7560548</td>
    <td>0.0590335</td>
</tr>
</table>

Set of results for images depicting circles that should be obvious for
the classifier to classify. Network handles the task well.

<table>
<tr>
    <th>Image</th>
    <td><img src="http://farm1.static.flickr.com/171/438599715_f0acd021ae.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm4.static.flickr.com/3165/2949285928_8a309f9493.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm5.static.flickr.com/4132/4999928992_4ba573a5f6.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm4.static.flickr.com/3589/3682046286_2f760da30b.jpg" alt="HTML5 Icon" width="150" height="150"></td>
</tr>

<tr>
    <th>Triangle</th>
    <td>0.0000078</td>
    <td>0.0001376</td>
    <td>0.0854333</td>
    <td>0.0000162</td>
</tr>

<tr>
    <th>Circle</th>
    <td>0.9999921</td>
    <td>0.9998624</td>
    <td>0.9145667</td>
    <td>0.9999838</td>
</tr>
</table>

<table>
<tr>
    <th>Image</th>
    <td><img src="http://farm1.static.flickr.com/3/3723630_86371af698.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm5.static.flickr.com/4012/4255939729_8caba9b07c.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm3.static.flickr.com/2729/4212306542_fc3f65d4d0.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm5.static.flickr.com/4004/4295748814_5c3554c22e.jpg" alt="HTML5 Icon" width="150" height="150"></td>
</tr>

<tr>
    <th>Triangle</th>
    <td>0.4076157</td>
    <td>0.0000519</td>
    <td>0.0000001</td>
    <td>0.0000024</td>
</tr>

<tr>
    <th>Circle</th>
    <td>0.5923843</td>
    <td>0.9999480</td>
    <td>0.9966859</td>
    <td>0.9999999</td>
</tr>
</table>

Set of results for images containing oval and triangulish shapes. I
was wondering how the classifier will react to those mixed pictures.
As it occurs, the network seems to be more into circles, unless shape
of a triangle is an obvious, plane case without any unusual perspective.
It may come from a fact that in training/testing set, the triangles
were underrepresented and treated only simple cases.
<table>
<tr>
    <th>Image</th>
    <td><img src="http://farm4.static.flickr.com/3243/3367977848_136586004a.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm2.static.flickr.com/1329/4603472286_cd8b9521ac.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm4.static.flickr.com/3442/3356045299_718107585e.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="https://s-media-cache-ak0.pinimg.com/736x/46/ef/3b/46ef3be35e81e6acf4570d39bf488420.jpg" alt="HTML5 Icon" width="150" height="150"></td>
</tr>

<tr>
    <th>Triangle</th>
    <td>0.0006555</td>
    <td>0.4060124</td>
    <td>0.0000001</td>
    <td>1.0000000</td>
</tr>
<tr>
    <th>Circle</th>
    <td>0.9993445</td>
    <td>0.5939876</td>
    <td>0.9999999</td>
    <td>0.0000000</td>
</tr>
</table>

<table>
<tr>
    <th>Image</th>
    <td><img src="http://farm6.static.flickr.com/5028/5619935182_a0763fb8bf.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://araischool.up.seesaa.net/image/109.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://www.uh.edu/engines/icosahedron.jpg" alt="HTML5 Icon" width="150" height="150"></td>
    <td><img src="http://farm5.static.flickr.com/4127/5199584958_a7043537d9.jpg" alt="HTML5 Icon" width="150" height="150"></td>
</tr>
<tr>
    <th>Triangle</th>
    <td>0.0016108</td>
    <td>0.0216434</td>
    <td>0.0002671</td>
    <td>0.0294803</td>
</tr>
<tr>
    <th>Circle</th>
    <td>0.9983892</td>
    <td>0.9783567</td>
    <td>0.9997329</td>
    <td>0.9705198</td>
</tr>
</table>