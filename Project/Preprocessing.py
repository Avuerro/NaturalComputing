###################
##### IMPORTS #####
###################

# Data processing and plotting
from tensorflow.keras.datasets import mnist, fashion_mnist
from skimage.transform import resize

# Standard python imports
import argparse, pickle, os, cv2
import numpy as np



######################
##### PARAMETERS #####
######################

parser = argparse.ArgumentParser()

# Dataset parameters
parser.add_argument("-d", type=str, dest="dataset", default="MNIST", help="Which dataset to use ('MNIST' or 'Fashion-MNIST')")
parser.add_argument("-s", type=int, dest="desired_image_size", default=(16,16), help="Desired image size (as a tuple)")
parser.add_argument("-c", type=int, dest="n_classes_to_use", default=10, help="Number of classes to keep (only the first n classes will be kept")

args = parser.parse_args()



##############################
##### PREPROCESSING DATA #####
##############################

##### DOWNLOADING THE CORRECT DATASET #####

# Load the data
(X_train, Y_train), (X_test, Y_test) = mnist.load_data() if args.dataset == "MNIST" else fashion_mnist.load_data()



##### REMOVING CLASSES #####

# Ensure correct number of classes
X_train = X_train[Y_train < args.n_classes_to_use]
Y_train = Y_train[Y_train < args.n_classes_to_use]
X_test = X_test[Y_test < args.n_classes_to_use]
Y_test = Y_test[Y_test < args.n_classes_to_use]

# Extract and print the number of training and testing samples remaining
n_samples_train = X_train.shape[0]
n_samples_test = X_test.shape[0]
print(f"Training samples remaining: {n_samples_train}")
print(f"Testing samples remaining: {n_samples_test}")



##### RESCALING, UNSKEWING & RESIZING #####

# This preprocessing procedure is heavily based on the one used in WANN:
# https://github.com/google/brain-tokyo-workshop/blob/master/WANNRelease/WANN/domain/classify_gym.py

def preprocess(samples, size, n_samples, unskew=True):
    # Create list of processed images
    processed  = np.empty((n_samples,size[0],size[1]))

    # Unskew and resize
    if unskew == True:    
        for i in range(n_samples):
            processed[i,:,:] = deskew(cv2.resize(samples[i,:,:],size),size)
    return processed

def deskew(image, image_shape, negated=True):
    """ source: https://github.com/vsvinayak/mnist-helper """
  
    # negate the image
    if not negated:
        image = 255-image
    
    # calculate the moments of the image
    m = cv2.moments(image)
    if abs(m['mu02']) < 1e-2:
        return image.copy()
    
    # caclulating the skew
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*image_shape[0]*skew], [0,1,0]])
    img = cv2.warpAffine(image, M, image_shape, flags=cv2.WARP_INVERSE_MAP|cv2.INTER_LINEAR)  
    return img

# Rescale and preprocess training and testing data
X_train_processed = preprocess(X_train/255, args.desired_image_size, n_samples_train)
X_test_processed = preprocess(X_test/255, args.desired_image_size, n_samples_test)
    
    

##### WRAPPING UP #####
    
# Replace and reshape X_train and X_test, for convenience
X_train = X_train_processed.reshape(n_samples_train, np.prod(args.desired_image_size))
X_test = X_test_processed.reshape(n_samples_test, np.prod(args.desired_image_size))

# Check if data folder exists; if not, create it
if not os.path.exists("data"):
    os.mkdir("data")
    
# Set the correct filename
filename = f"{args.dataset}-{args.n_classes_to_use}.pkl"

# Store the preprocessed data
with open(os.path.join("data", filename), "wb") as f:
    pickle.dump(((X_train, Y_train), (X_test, Y_test)), f)