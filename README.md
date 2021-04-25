# Fingerprints

This is research and implementation of a fingerprint minutiae extraction algorithm.
The implementation follows [[1]](#1) in the most part, but it is adding my own original ideas in combination with some major ideas from [[2]](#2) and [[3]](#3). The image data is taken from [[4]](#4).

## Algorithm
1. Take a raw image of a fingerprint

    In this case they are directly taken from [[4]](#4)

2. Enhance and binarize the raw image

    Implementation of this is object of future work and research. For now the library **fingerprint-enhancer** is used for that. More information of the enhancement algorithm can be obtained from [[2]](#2) 

3. Morphological preprocessing

    The preprocessing consists of three steps
    1. Spur removal -> done with pruning
    2. Hole removal -> done with morphological opening
    3. Islands removal -> done with morphological closing

4. Thinning

    Morphological thinning with Hit&Miss transform. Skeletonization with opening would leave many line breaks and false minutiae, so Hit&Miss thinning is preferred.

5. Minutiae extraction

    For terminations and bifurcations we use use different set of kernels.
    Apply Hit&Miss with the corresponding kernels for extract the minutiae.

6. Morphological post-processing

    The previous steps may leave some false minutiae. This is why we need to get rid of them. Using three terminations. T1 - remove terminations which have distance between them less than T1. T2 - remove bifurcations that have distance between them less than T2. T3 - remove termination and bifurcations that have distance between them less than T3.


The main implementation is in **fingerprints.py**. Important part of the algorithm is the set of kernels chosen for the morphological operations. In **fingerprints_kernels.py** are all the kernel sets that are used.

## Dependencies
* [Open CV](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/stable/index.html)
* [Fingerprint-Enhancer](https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python)

## References
<a id="1">[1]</a>
Roli Bansal, Priti Sehgal & Punam Bedi - Effective Morphological Extraction of True Fingerprint Minutiae based on the Hit or Miss Transform

<a id="2">[2]</a>
Lin Hong, Student Member, IEEE, Yifei Wan, and Anil Jain, Fellow, IEEE - Fingerprint Image Enhancement: Algorithm and Performance Evaluation

<a id="3">[3]</a>
Pu Hongbin Chen Junali Zhang Yashe - Fingerprint Thinning Algorithm Based on Mathematical Morphology

<a id="4">[4]</a>
[FVC fingerprint database](http://bias.csr.unibo.it/fvc2004/)

<a id="5">[5]</a>
Letian Cao and Yazhou Wang, Sven Nordebo - Fingerprint image enhancement and minutiae extraction algorithm
