# parallel-image-processing-algorithms
parallel image processing algorithms using PyMP and OpenMP

The following algorithms were parallelized:

1. Gaussian Blurring

2. Otsu thresholding

3. Sobel edge detection algorithm

All the algorithms were implemented serially in Python and parallelized using PyMP(https://github.com/classner/pymp).
Otsu thresholding was implemented in C as well, both serially and parallely using OpenMP (https://computing.llnl.gov/tutorials/openMP/).
The speedup achieved in Python (using PyMP) was found to be better in comparison to speedup achieved in C (using OpenMP).

Here are the description of files:

gbpar.py => parallel implementation of Gaussian blurring

gbser.py => serial implementation of Gaussian blurring

mypgm_omp.h => header file for C for image reading, writing, saving etc.

otsu.py => serial implemetation of Otsu thresholding in C

otsup.py => parallel implemetation of Otsu thresholding in C

sobel.py => serial implementation of sobel operator

sobelser.py => parallel implementation of sobel operator
