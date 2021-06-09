# Natural Computing - Weight Agnostic Neural Networks
#### Group 25: Chihab Amghane, Max Driessen, Jordy Naus

## Description

This repo contains all the code used for the project part of the Natural Computing course at the Radboud University (NWI-IMC042-2020).
The project is an exploratory study in creating Weight Agnostic Neural Networks (WANNs), and is mostly inspired by [this work done by Google](https://weightagnostic.github.io).
In total, three algorithms have been implemented and compared with Google's WANN implementation as baseline.
On top of that, these implementations have been extended to a more complex classification task, namely Fashion-MNIST.

## Structure

The repo contains 9 notebooks, and one Python source code file.

First, both the notebook named ```preprocessing.ipynb``` and the source file ```preprocessing.py``` have been used to create the preprocessing pipeline.
Both work the same, although the notebook contains visuals to show the preprocessing pipeline.

Next, the three custom implementations each have two separate notebooks. 
One notebook for testing the method on MNIST, and another to test the method on Fashion-MNIST.
Generally, the naming scheme for the notebooks is as follows:

```METHOD-DATASET.ipynb```,

where `METHOD` can be either one of the following:
 - DEAP;
 - DEAPWANN;
 - NEAT.

On top of that, `DATASET` can be one of the following:
 - MNIST;
 - Fashion-MNIST.

Finally, there are two results notebooks, that were used to generate the result plots, and these are named as follows:

```DATASET Results.ipynb```,

where `DATASET` can be, again, one of the following:
 - MNIST;
 - Fashion-MNIST.

Besides these files, we have the following folders:

 - `NEAT-configs`, which  contains the configuration file for running the NEAT algorithm.
 - `NEAT-results`, which contains the raw results for the NEAT algorithm after running the algorithm.
 - `WANN`, which contains the source code for running the WANN algorithm.
 - `imgs`, which contains images of the results of the project.
 - `screenshots`, which is now empty, but will be filled with example screenshots of system behavior.

## How to Run

### Preprocessing
Before running any notebook, the notebook ```preprocessing.ipynb``` should be executed, since this notebook makes sure the correct data is downloaded, preprocessed and saved.
In this notebook, there is a global parameter named `DATASET`, which can be set to `MNIST` or `Fashion-MNIST`, depending on which dataset you want to download and preprocess.

### DEAP, NEAT, WANNDEAP
After this, using this repo is simply a matter of running any of the notebooks, depending on which method and dataset you want to run.
The data needed to run these notebooks is either provided in the notebook, or it has been preprocessed before by executing ```preprocessing.ipynb```.

### WANN

Running WANN code is a bit harder, and Python 3.5 is needed to do so.
When you are in an environment that supports Python 3.5, WANN can be ran with the following command:

```python wann_train.py -p p/DATASET.json -n 8```,
where `DATASET` can be, again, one of the following:
 - MNIST;
 - Fashion-MNIST.

## Screenshots of System Behavior

For each implementation, a screenshot will be shown while running the MNIST dataset, as an example of how the system behavior should look like.

### Preprocessing

![preprocessing](https://github.com/Avuerro/NaturalComputing/blob/main/Project/screenshots/preprocessing.png "Results of performing preprocessing")

### DEAP

![deap](https://github.com/Avuerro/NaturalComputing/blob/main/Project/screenshots/DEAP.png "System behavior of DEAP")

### NEAT

![neat](https://github.com/Avuerro/NaturalComputing/blob/main/Project/screenshots/NEAT.png "System behavior of NEAT")

### DEAPWANN

![deapwann](https://github.com/Avuerro/NaturalComputing/blob/main/Project/screenshots/DEAPWANN.png "System behavior of DEAPWANN")

### WANN

![wann](https://github.com/Avuerro/NaturalComputing/blob/main/Project/screenshots/WANN.png "System behavior of WANN")