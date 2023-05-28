# Image Classifier

This repository contains an image classification project implemented using popular deep learning models such as VGG, AlexNet, and ResNet. The project aims to classify images into different predefined categories based on their content.

## Problem Statement:

> Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant who registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information. Some people are planning on registering pets that aren’t actual dogs.

### Task in hand:

1. To classify images using various CNN models.
2. To note the image labels for comparison of actual values for performance calculations.
3. To know whether it is a dog or not.
4. To know which breed of dog it is (if it's a dog).


## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Dataset](#dataset)


## Installation

To get started with the Image Classifier project, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Sreeja799/Image-Classifier.git
   ```

2. Install the required dependencies. It is recommended to set up a virtual environment before installing the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Download the dataset (see [Dataset](#dataset) section for more information) and place it in the appropriate location within the project directory.

4. The project is now ready to use!

## Usage

Before using the Image Classifier project, make sure you have completed the installation steps mentioned above.

To train and evaluate the image classification models, follow these instructions:

1. Open the terminal and navigate to the project directory.

2. To train a specific model (e.g., VGG), run the following command:

   ```
   python train.py --model vgg
   ```

   This will initiate the training process for the VGG model using the default settings. You can modify the hyperparameters and training configurations as needed.

3. Once the training is complete, you can evaluate the trained model on a test dataset using the following command:

   ```
   python evaluate.py --model vgg
   ```

   This will evaluate the VGG model's performance and provide metrics such as accuracy and loss.

4. You can repeat the above steps for the other available models (AlexNet and ResNet) by replacing `vgg` with `alexnet` or `resnet` in the commands.

Feel free to explore and modify the code to suit your specific requirements.

## Models

The Image Classifier project implements the following deep learning models for image classification:

- **VGG**: The VGG (Visual Geometry Group) model is known for its simplicity and effectiveness. It consists of multiple convolutional layers followed by fully connected layers.

- **AlexNet**: AlexNet was a groundbreaking model that won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2012. It introduced the concept of deep convolutional neural networks and demonstrated their superiority in image classification tasks.

- **ResNet**: ResNet (Residual Neural Network) is a deep learning architecture known for its ability to train very deep networks. It introduced residual connections, which alleviate the problem of vanishing gradients and enable the training of deeper models.

Each model comes with its own set of strengths and weaknesses, and the choice of which model to use depends on the specific requirements of your image classification task.

## Dataset

The Image Classifier project uses a dataset of labeled images for training and evaluation.

### Conclusion: 

By my observation of dog image classification, VGG works the best compared to the other two models.
