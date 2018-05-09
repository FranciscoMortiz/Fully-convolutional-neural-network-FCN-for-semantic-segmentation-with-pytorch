# Run prediction and genertae pixelwise annotation for every pixels in the image based rgb  image
# Output saved as label images, and label overlay on the original image
# 1) Make sure you you have trained model in Trained_model_path (See Train.py for creating trained model)
# 2) Set the Image_Dir to the folder where the input image for prediction are located
# 3) Set number of classes number in NUM_CLASSES
# 4) Set Output_Dir the folder where you want the output annotated images to be save
# 5) Run script
#-----------------------Imports---------------------------------------------------------------------------------------------
import numpy as np
import scipy.misc as misc
import os
import Data_Reader
import OverrlayLabelOnImage as Overlay
import NET_FCN
import torch
#------------------------Input Parameters-------------------------------------------------------
Image_Dir="Data_Zoo/Materials_In_Vessels/Test_Images_All/"# Test image folder
Trained_model_path="TrainedModelWeights/20000.torch"# "Path to trained net weights
w=0.5# weight of overlay on image for display
Output_Dir="Output_Prediction/" #Folder where the output prediction will be save
NameEnd="" # Add this string to the ending of the file name optional
NUM_CLASSES = 4 # Number of classes
#-----------------------------Create net and load weight--------------------------------------------------------------------------------------------
Net = NET_FCN.Net(NumClasses=NUM_CLASSES) #Build net
Net.load_state_dict(torch.load(Trained_model_path)) #-Load Trained model weight if you dont have trained model see: Train.py
print("Model weights loaded from: "+Trained_model_path)
################################################################################################################################################################################

# -------------------------Data reader for validation/testing images-----------------------------------------------------------------------------------------------------------------------------
ValidReader = Data_Reader.Data_Reader(Image_Dir, BatchSize=1)

#--------------------Create output folders for predicted label, one folder for each granulairy of label prediciton---------------------------------------------------------------------------------------------------------------------------------------------

if not os.path.exists(Output_Dir): os.makedirs(Output_Dir)
if not os.path.exists(Output_Dir+"/OverLay"): os.makedirs(Output_Dir+"/OverLay")
if not os.path.exists(Output_Dir + "/Label"): os.makedirs(Output_Dir + "/Label")


print("Running Predictions:")
print("Saving output to:" + Output_Dir)
#----------------------Go over all images and predict semantic segmentation in various of classes-------------------------------------------------------------
fim = 0
print("Start Predicting " + str(ValidReader.NumFiles) + " images")
while (ValidReader.itr < ValidReader.NumFiles):
    print(str(fim * 100.0 / ValidReader.NumFiles) + "%")
    fim += 1
    # ..................................Load image.......................................................................................
    FileName=ValidReader.OrderedFiles[ValidReader.itr] #Get input image name
    Images = ValidReader.ReadNextBatchClean()  # load testing image

    # Predict annotation using net
    Prob, Pred = Net.forward(Images)  # Predict annotation using net
    LabelPred = np.array(Pred.data)
    #------------------------Save predicted labels overlay on images---------------------------------------------------------------------------------------------
    misc.imsave(Output_Dir + "/OverLay/"+ FileName+NameEnd  , Overlay.OverLayLabelOnImage(Images[0],LabelPred[0], w)) #Overlay label on image and save
    misc.imsave(Output_Dir + "/Label/" + FileName[:-4]+".png" + NameEnd, LabelPred[0].astype(np.uint8)) #Save annotation map
    ##################################################################################################################################################