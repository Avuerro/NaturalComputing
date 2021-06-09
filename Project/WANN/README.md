# Weight Agnostic Neural Networks

The code used to run the WANN implementation can be found in this folder, all the instructions below are still valid but there is only one caveat. If you would like to run the network on fashionmnist or mnist data, please download the data first, then modify the locations in the classify_gym module. To be precise, you should change [mnist_256](https://github.com/Avuerro/NaturalComputing/blob/e16e4918d59195e9bba238b83d755a6751830d0c/Project/WANN/domain/classify_gym.py#L123) and [fashion_mnist](https://github.com/Avuerro/NaturalComputing/blob/e16e4918d59195e9bba238b83d755a6751830d0c/Project/WANN/domain/classify_gym.py#L135).

## Dependencies

Core algorithm tested with:

- Python 3.5.3

- NumPy 1.15.2 (`pip install numpy`)

- mpi4py 3.0.1 (`pip install mpi4py`)

- OpenAI Gym 0.9.6 (`pip install gym` -- installation details [here](https://github.com/openai/gym))


Domains tested with:

- MNIST
- Fashion MNIST

## Training Weight Agnostic Neural Networks
If you would like to train the model on the MNIST data run the following command:

```
python wann_train.py -p p/mnist256.json -n 8
```
Where `8` is the number of workers you have on your computer, and `p/mnist256.json` contains hyperparameters for the MNIST task. If you would like to train the model on the Fashion MNIST task, you can use the following commands

```
python wann_train.py -p p/fashion_mnist.json -n 8
```
If you would like to change the number of generations or population size, check the .json hyperparameter files and modify the values. There are multiple values that can be tweaked, such as tournament size and the number of times you would like to run the model. If you would like to experiment with the hyperparameters check out ```hypkey.txt``` and ```default_wann.json``` in the _p_ directory.


## Testing Weight Agnostic Neural Networks and Analyzing performance

If you would like to test the network on the mnist or fashionmnist data you should call the [evaluateModel method](https://github.com/Avuerro/NaturalComputing/blob/0d00725c1f744b04c823e383d7d8336bb8856109/Project/WANN/wann_src/task.py#L143). Please see the following notebooks for examples of how to test the model, [mnist](https://github.com/Avuerro/NaturalComputing/blob/main/Project/WANN/Mnist%20Performance%20Statistics.ipynb) and [fashionmnist](https://github.com/Avuerro/NaturalComputing/blob/main/Project/WANN/Fashion-Mnist%20Performance%20Statistics.ipynb). The notebooks also contain code to analyze the results. 

### Analysing the input pixels used by the model.

If you are interested in which pixels are used for which class by the model, you should run the [usedInputs method](https://github.com/Avuerro/NaturalComputing/blob/30cebfb059ec74fad595ca526b4133763729b541/Project/WANN/wann_src/task.py#L195). This method will return a dictionary where the keys are the classes and each value is a list containing the input pixels used for that class. If you would like to go one step further and recreate the tree, e.g. determine which _functions_ the tree consist of, you could utilize the activationVector which contains the activation function of each node. However, keep in mind that determining which _functions_ the tree consists of is an experimental part of the code.

Adam Gaier and David Ha.  Weight agnostic neural networks.  2019.https://weightagnostic.github.io

