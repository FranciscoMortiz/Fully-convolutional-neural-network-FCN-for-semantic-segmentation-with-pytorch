# Fully convolutional neural network (FCN) for semantic segmentation with pytorch.

Fully convolutional neural network (FCN) for pixelwise annotation (semantic segmentation) of images implemented on python pytorch. 
 

## Details input/output
The input for the net is RGB image (Figure 1 right).
The net produces pixel-wise annotation as a matrix in the size of the image with the value of each pixel corresponding to its class (Figure 1 left).

![](/Figure1.png)
Figure 1) Semantic segmentation of image of liquid in glass vessel with FCN. Red=Glass, Blue=Liquid, White=Background

## Requirements
This network was run with Python 3.6  [Anaconda](https://www.anaconda.com/download/) package and [Pytorch 0.3](https://pytorch.org/). The training was done using Nvidia GTX 1080, on Linux Ubuntu 16.04.

## Setup
1) Install [Pytorch](https://pytorch.org/)
2) Download the code from the repository.
3) Download pretrained DenseNet model for net initiation from: [https://drive.google.com/file/d/1bFdIbIS_2pWd9PQs1x_hYq6Y0BVsL2eI/view?usp=sharing]
    and put in Pretrained_Encoder_Weights folder

## Tutorial

### Instructions for training (in TRAIN.py):
In: TRAIN.py
1) Download pretrained DenseNet model for net initiation from: [https://drive.google.com/file/d/1bFdIbIS_2pWd9PQs1x_hYq6Y0BVsL2eI/view?usp=sharing]
    and put in Pretrained_Encoder_Weights folder
2) Set folder of training images in Train_Image_Dir
3) Set folder for ground truth labels in Train_Label_DIR
   The Label Maps should be saved as png image with same name as the corresponding image in Train_Image_Dir and png ending (the pixel value should be its label)
4) Set number of classes the net can predict in number in NUM_CLASSES
5) If you are interested in using validation set during training, set UseValidationSet=True and the validation image folder to Valid_Image_Dir
6) Run script
See additional parameters you can playu with in the input parameters section of the train.py script

### Instructions for predicting pixelwise annotation using trained net (in Inference.py)
In: Inference.py
1) Make sure you you have trained model in Trained_model_path (See Train.py for creating trained model)
2) Set the Image_Dir to the folder where the input image for prediction are located
3) Set number of classes number in NUM_CLASSES
4) Set Output_Dir the folder where you want the output annotated images to be save
5) Run script

### Evaluating net performance using intersection over union (IOU):
In: Evaluate_Net_IOU.py
1) Make sure you you have trained model in Trained_model_path (See Train.py for training model)
2) Set the Image_Dir to the folder where the input images for prediction are located
3) Set folder for ground truth labels in Label_DIR
    The Label Maps should be saved as png image with same name as the corresponding image and png ending
4) Set number of classes number in NUM_CLASSES
5) Set classes names in Classes
6) Run script
## Net Architecture
The net is composed on [Densenet](https://arxiv.org/pdf/1608.06993.pdf) encoder [PSP](https://arxiv.org/pdf/1612.01105.pdf) itermediate layers  and two [deconvolutional](https://arxiv.org/pdf/1605.06211.pdf) upsample layers. The net architecture is defined in the NET_FCN.py file. The Densenet encoder is defined in densenet_cosine_264_k32.py.
## Supporting data sets
The net was tested on a dataset of annotated images of materials in glass vessels. 
This dataset can be downloaded from [here](https://drive.google.com/file/d/0B6njwynsu2hXRFpmY1pOV1A4SFE/view?usp=sharing)

MIT Scene Parsing Benchmark with over 20k pixel-wise annotated images can also be used for training and can be download from [here](http://sceneparsing.csail.mit.edu/)

   
# Fully-convolutional-neural-network-FCN-for-semantic-segmentation-with-pytorch