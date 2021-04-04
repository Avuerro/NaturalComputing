# Natural Computing - Assignment 4
## Cellular Automata - Making a Cellular Potts Model of Collective Migration
#### Solutions team 25: Chihab Amghane, Max Driessen, Jordy Naus

This folder contains our code for the Cellular Automata assignment of the Natural Computing course. All folders include `artistoo(-cjs).js` and `fpsmeter.min.js`, as these files are required to run the simulation. These files were retrieved from [the Artistoo GitHub repository](https://github.com/ingewortel/artistoo).  
+ The `Simulation Random` folder contains all code required to run the "Random" simulation, where cells move randomly.
+ The `Simulation Target` folder contains all code required to run the "Target" simulation, where cells move from left to right.
+ The `Simulation NodeJS` folder contains all code required to run the "Target" simulation in NodeJS to obtain accurate frame timing measurements. `run.py` contains some python code for running our experiment (the number of initial cells should be changed manually). The `commands.txt` file contains the commands used to run the code and create videos from the generated frames. Note: you might need to install some NodeJS modules before running this code.