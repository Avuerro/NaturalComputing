# Weight Agnostic Neural Networks

The code used to run the WANN implementation can be found in this folder, all the instructions below are still valid but there is only one caveat. If you would like to run the network on fashionmnist or mnist data, please download the data first, then modify the locations in the classify_gym module. To be precise, you should change [mnist_256](https://github.com/Avuerro/NaturalComputing/blob/e16e4918d59195e9bba238b83d755a6751830d0c/Project/WANN/domain/classify_gym.py#L123) and [fashion_mnist](https://github.com/Avuerro/NaturalComputing/blob/e16e4918d59195e9bba238b83d755a6751830d0c/Project/WANN/domain/classify_gym.py#L135).

Weight Agnostic Networks: network topologies evolved to work with a variety of shared weights. Adapted from the [prettyNEAT](../prettyNEAT) package. This repository represents a snapshot of the code used to produce the results in the original [WANN paper](https://weightagnostic.github.io/). The goal was to create minimal rather than general code for clearer understanding. If you are interested in a more extendable and general implementation for your own experiments, we recommend using the [WANN fork](../prettyNEAT_WANN) of the [prettyNEAT](../prettyNEAT) package.

## Dependencies

Core algorithm tested with:

- Python 3.5.3

- NumPy 1.15.2 (`pip install numpy`)

- mpi4py 3.0.1 (`pip install mpi4py`)

- OpenAI Gym 0.9.6 (`pip install gym` -- installation details [here](https://github.com/openai/gym))


Domains tested with:

- Cart-pole Swing-up (included, but requires OpenAI gym)

- Bipedal Walker: Box2d (see OpenAI gym installation)

- Quadruped (Ant) Walker: PyBullet 1.6.3 (`pip install pybullet`)

- MNIST: Mnist utilities 0.2.2 (`pip install mnist`)

- VAE Racer: 
    - Tensorflow 1.8 (`pip install tensorflow==1.8.0`)
    - Pretrained VAE (in [wannRelease](../) -- copy to root to use, e.g: `cp -r ../vae .`)



## Training Weight Agnostic Neural Networks

To get started and see that everything is set up you can test the swing up domain:

```
python wann_train.py
```

which is the same as the default hyperparameter:

```
python wann_train.py -p p/laptop_swing.json -n 8
```

Where `8` is the number of workers you have on your computer, and `p/laptop_swing.json` contains hyperparameters.


## Testing Weight Agnostic Neural Networks and Analyzing performance

If you would like to test the network on the mnist or fashionmnist data you should call the [evaluateModel method](https://github.com/Avuerro/NaturalComputing/blob/0d00725c1f744b04c823e383d7d8336bb8856109/Project/WANN/wann_src/task.py#L143). Please see the following notebooks for examples of how to test the model, [mnist](https://github.com/Avuerro/NaturalComputing/blob/main/Project/WANN/Mnist%20Performance%20Statistics.ipynb) and [fashionmnist](https://github.com/Avuerro/NaturalComputing/blob/main/Project/WANN/Fashion-Mnist%20Performance%20Statistics.ipynb). The notebooks also contain code to analyze the results. 


Adam Gaier and David Ha.  Weight agnostic neural networks.  2019.https://weightagnostic.github.io

