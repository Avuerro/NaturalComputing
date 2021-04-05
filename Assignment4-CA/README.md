# Natural Computing - Assignment 4
## Cellular Automata - Making a Cellular Potts Model of Collective Migration
#### Solutions team 25: Chihab Amghane, Max Driessen, Jordy Naus

This folder contains our code for the Cellular Automata assignment of the Natural Computing course. The folders include `artistoo(-cjs).js` (and `fpsmeter.min.js`), as these files are required to run the simulation. These files were retrieved from [the Artistoo GitHub repository](https://github.com/ingewortel/artistoo).  
+ The `Simulation HTML` folder contains all code required to run our simulation in HTML, which can be useful for interactivity.
+ The `Simulation NodeJS` folder contains all code required to run our simulation in NodeJS to obtain accurate frame timing measurements; this is the simulation we used in our experiment. 
	+ `run.py` contains some python code for running our experiment (the number of initial cells should be changed manually). 
	+ `commands.txt` contains the commands used to run the code and create videos from the generated frames. Note: you might need to install some NodeJS modules before running this code.
	+ `extract_important.py` extracts each frame that is a multiple of 100 and adds the goal line to it, so that you can check the number of cells that have reached the goal.