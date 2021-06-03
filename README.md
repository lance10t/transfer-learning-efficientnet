# Explanation on model
## Introduction
The task of our assignment is to build an Image Classifier for photos that have been captured by SMU Undergraduates and Graduate students.  The images are from a total of 72 classes, and have already been pre-arranged into sub-folders where each of the folder names will be the label that is used.

This submission uses the [EfficientNetB5 algorithm](https://ai.googleblog.com/2019/05/efficientnet-improving-accuracy-and.html), which manages to achieve superior performance vs competing algorithms with lesser parameters (see diagram below).  This speeds up training time significantly while allowing researchers to try different model prototypes.

![model_size_vs_accuracy.png](attachment:4042a9cd-bf36-4368-9295-240b17d33abf.png)

## Data Used
The data provided as part of this assignment had been split up into 72 subfolders, with the name of the subfolder as the class name.  Prior to the start of the training, we had performed the following data preparation as it aided in the flow and also sped up the training else the bottleneck becomes the CPU-intensive task of resizing the full-sized pictures into 456x456 images.  In earlier runs, the CPU could not feed the images fast enough to the GPU for training, and each repeated run went through the same unncessary process of resizing again.

Thus, we had performed the following:

1. Create a train-val-test subfolder structure using the splitfolders Python package.  The package can be downloaded from the [PyPi repository](https://pypi.org/project/split-folders/)
2. Ran the helper script to resize the images in these folders to the desired size.  In the setup, we had created a few sets of image sizes as we wanted to experiment with different EfficientNetB* algorithms, each requiring different image sizes as highlighted below:

![Screenshot 4-15-21 at 11.50.26 AM.png](attachment:afba43e7-d348-47e3-be1d-4edfeaf7eae7.png)

## Training Phases
We perform the training in two distinct steps.

### Phase 1 - Using pre-trained weights to arrive at a quick model
We create the initial model from the EfficientNetB5 model, with <code>include_top=False</code>.  We will rebuild our own "top" layer which comprises the GlobalAveragePooling, Dropout (20%), and connected to a final (NUM_CLASS,) Dense layer to perform a softmax computation.  

We freeze the original model with the exception of the final layer as we will then use this to quickly learn the weights based on the pre-trained model (pre-trained on ImageNet).

In this phase, we run 50 epochs and the learning rate can be fairly high at 1e-02.

### Phase 2 - Unfreeze Block7a onwards and perform fine-tune training
After we have arrived at a rough model, we then unfreeze Block 7 of the EfficientNetB5.  Because of the skip connections, we must ensure that we unfreeze the **ENTIRE** block, and also to freeze back any BatchNormalization layers.  This is achieved in the unfreeze_model() code in this notebook.

We then **CONTINUE** running the training with a reduced learning rate of 1e-04 for another 50 epochs.  You can see from the accuracy history charts that after a period of plateued performance in Phase 1, the accuracy increases again with this refined phase.

## 


The concepts here are inspired by the official [Tensorflow tutorials](https://www.tensorflow.org/tutorials/images/transfer_learning) on using Transfer Learning to adapt models quickly.

https://www.tensorflow.org/tutorials/images/transfer_learning
