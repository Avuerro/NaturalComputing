###################
##### IMPORTS #####
###################

# Data processing and plotting
from tensorflow.keras.datasets import mnist, fashion_mnist
from skimage.transform import resize

# Standard python imports
import argparse, pickle, os
import numpy as np



######################
##### PARAMETERS #####
######################

parser = argparse.ArgumentParser()

# Dataset parameters
parser.add_argument("-d", type=str, dest="dataset", default="MNIST", help="Which dataset to use (MNIST or Fashion-MNIST)")
parser.add_argument("-s", type=int, dest="desired_image_size", default=16, help="Desired image size (shape will be size x size")
parser.add_argument("-c", type=int, dest="n_classes_to_use", default=4, help="Number of classes to keep (only the first n classes will be kept")

# Processing parameters
parser.add_argument("--aa", action="store_true", dest="do_anti_aliasing", help="Perform anti-aliasing")
parser.add_argument("--n", action="store_true", dest="do_normalization", help="Perform normalization")

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


##### RESCALING #####

# Rescaling to the desired size
def rescale_images(images):
    desired_image_shape = (args.desired_image_size, args.desired_image_size)
    return np.array([resize(image, desired_image_shape, anti_aliasing=args.do_anti_aliasing) for image in images])

# Rescale X_train and X_test
X_train_small = rescale_images(X_train)
X_test_small = rescale_images(X_test)


##### NORMALIZATION #####

# Normalizing data
def normalize(images):
    return (images - np.mean(images, axis=0))/(np.std(images, axis=0) + 0.000001)

# Normalize X_train_small and X_test_small, if required
if args.do_normalization:
    X_train_norm = normalize(X_train_small)
    X_test_norm = normalize(X_test_small)
    

##### WRAPPING UP #####
    
# Replace and reshape X_train and X_test, for convenience
X_train = (X_train_norm if args.do_normalization else X_train_small).reshape(n_samples_train, args.desired_image_size**2)
X_test = (X_test_norm if args.do_normalization else X_test_small).reshape(n_samples_test, args.desired_image_size**2)

# Check if data folder exists; if not, create it
if not os.path.exists("data"):
    os.mkdir("data")
    
# Set the correct filename
filename = f"{args.dataset}-{args.n_classes_to_use}{'-Norm' if args.do_normalization else ''}" + \
           f"{'-AA' if args.do_anti_aliasing else ''}.pkl"

# Store the preprocessed data
with open(os.path.join("data", filename), "wb") as f:
    pickle.dump(((X_train, Y_train), (X_test, Y_test)), f)