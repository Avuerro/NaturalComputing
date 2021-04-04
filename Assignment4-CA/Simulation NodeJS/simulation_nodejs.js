"use strict"

/****** Parameters ******/

let cellType, obstacleSpacing, nrCells, nrFrames, seed, outputFolderName
[cellType, obstacleSpacing, nrCells, nrFrames, seed, outputFolderName] = process.argv.slice(2)
let cellMaxAct = (cellType=="amoeba") ? 20:80
obstacleSpacing = parseInt(obstacleSpacing)
nrCells = parseInt(nrCells)
nrFrames = parseInt(nrFrames)
seed = parseInt(seed)

let extraWidth = 200
let goalImportance = 25


/****** Simulation Parameters ******/

let CPM = require("./artistoo-cjs.js")


let config = {

	// Grid settings
	ndim : 2,
	field_size : [250+extraWidth,250],
	
	// CPM parameters
	conf : {
		// Basic CPM parameters
		torus : [false,true],		// Grid has linked borders in both directions
		seed : seed,				// Seed for random number generation
		T : 20,						// CPM temperature
		
		// Adhesion parameters:
		J : [ [0,20,20],  			// Background
		      [20,0,0],				// Cells
			  [20,0,0] ],			// Obstacles
		
		// Volume parameters
		LAMBDA_V : [0,50,1000],		// Volume importances
		V : [0,500,250],			// Target volumes
		
		// Perimeter parameters
		LAMBDA_P : [0,2,1000],		// Perimeter importances
		P : [0,300,150],			// Target perimeters
		
		// Activity parameters
		LAMBDA_ACT : [0,200,0],		// Activity importances
		MAX_ACT : [0,cellMaxAct,0],	// Activity memories
		ACT_MEAN : "geometric"		// Neighborhood activity is computed as a "geometric" mean
	},
	
	// Simulation setup
	simsettings : {
	
		// Cells on the grid
		NRCELLS : [nrCells,0],				// Number of cells to seed (handled by buttons and initializeGrid)
		
		// Runtime information
		BURNIN : 50,						// How many frames to skip at the start
		RUNTIME : nrFrames,					// How many frames to run the simulation for			
		
		// Visualization
		CANVASCOLOR : "eaecef",				// Background color
		CELLCOLOR : ["888888","660000"],	// Cell colors
		ACTCOLOR : [true,false],			// Display pixel activity values
		SHOWBORDERS : [true,true],			// Display cell borders
		zoom : 2,							// Zoom level
		
		// Output images
		SAVEIMG : true,						// Save PNG of every frame
		IMGFRAMERATE : 1,					// Save PNG of every frame
		SAVEPATH : outputFolderName,		// Save PNG files in this folder
		EXPNAME : "frame",					// Filename of output images
	}
}



/******	Simulation Functions ******/

function initializeGrid(){
	// Add the initializer if not already there
	if( !this.helpClasses["gm"] ){ this.addGridManipulator(); }

	// Reset C and clear cache (important if this method is called again later)
	this.C.reset();
}

function populateGrid(){
	// Initialize obstacles
	for( let i = Math.floor(obstacleSpacing/2+extraWidth/2); i < sim.C.extents[0]-extraWidth/2 ; i += obstacleSpacing ){
		for( let j = Math.floor(obstacleSpacing/2); j < sim.C.extents[1] ; j += obstacleSpacing ){
			sim.C.setpix( [i,j], sim.C.makeNewCellID(2) )
		}
	}
	
	// Seed the right number of cells
	for( let i = 0; i < nrCells; i++ ){		
		seedCell( 1 );
	}
}

function seedCell( kind, max_attempts = 10000 ){
	// Find empty location for new cell (to the left of the obstacles)
	let p = [25, Math.floor(sim.C.extents[1]/2)]
	while( sim.C.pixt( p ) !== 0 && max_attempts-- > 0 ){
		for( let i = 0 ; i < p.length ; i ++ ){
			p[i] = sim.C.ran(0, (i == 0) ? Math.floor(extraWidth/2):sim.C.extents[1])
		}
	}
	
	// If no location found, return (failed)
	if( sim.C.pixt(p)  !== 0 ){
		return 
	}
	
	// Create new cell
	const newID = sim.C.makeNewCellID( kind );
	sim.C.setpix( p, newID );
}



/****** Running the simulation ******/

// Initialize simulation
let sim = new CPM.Simulation( config, {initializeGrid:initializeGrid} )

// Add goal (attraction point constraint)
let Cdir = new CPM.AttractionPointConstraint({
	LAMBDA_ATTRACTIONPOINT : [0,goalImportance,0],
	ATTRACTIONPOINT : [[0,0], [sim.C.extents[0]-25,sim.C.extents[1]/2], [0,0] ] 
})
sim.C.add( Cdir )

// Populate the grid with cells (cannot easily place cells only on the left within initializeGrid)
populateGrid()

// Run the simulation
sim.run()