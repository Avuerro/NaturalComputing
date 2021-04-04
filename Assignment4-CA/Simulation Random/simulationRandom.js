"use strict"

/****** Simulation Parameters ******/

let config = {

	// Grid settings
	ndim : 2,
	field_size : [250,250],
	
	// CPM parameters
	conf : {
		// Basic CPM parameters
		torus : [true,true],	// Grid has linked borders in both directions
		seed : 1,				// Seed for random number generation
		T : 20,					// CPM temperature
		
		// Adhesion parameters:
		J : [ [0,20,20],  		// Background
		      [20,0,0],			// Cells
			  [20,0,0] ],		// Obstacles
		
		// Volume parameters
		LAMBDA_V : [0,50,1000],	// Volume importances
		V : [0,500,250],		// Target volumes
		
		// Perimeter parameters
		LAMBDA_P : [0,2,1000],	// Perimeter importances
		P : [0,300,150],		// Target perimeters
		
		// Activity parameters
		LAMBDA_ACT : [0,200,0],	// Activity importances
		MAX_ACT : [0,80,0],		// Activity memories
		ACT_MEAN : "geometric"	// Neighborhood activity is computed as a "geometric" mean
	},
	
	// Simulation setup
	simsettings : {
	
		// Cells on the grid
		NRCELLS : [0,0],					// Number of cells to seed (handled by buttons and initializeGrid)
		
		// Visualization
		CANVASCOLOR : "eaecef",				// Background color
		CELLCOLOR : ["888888","660000"],	// Cell colors
		ACTCOLOR : [true,false],			// Display pixel activity values
		SHOWBORDERS : [true,true],			// Display cell borders
		zoom : 2,							// Zoom level
	}
}



/******	Simulation Functions ******/

let sim, meter
let numberOfObstacles
let spacing = 50

function initializeGrid(){
	// Add the initializer if not already there
	if( !this.helpClasses["gm"] ){ this.addGridManipulator(); }

	// Reset C and clear cache (important if this method is called again later)
	this.C.reset();
	
	// Extract number of cells of each type
	let nrcells = this.conf["NRCELLS"], cellkind, i;
	
	// Initialize obstacles
	numberOfObstacles=0
	let offset = Math.floor((this.C.extents[0]-spacing)%spacing/2)
	for( let i = Math.floor(spacing/2); i < this.C.extents[0] ; i += spacing ){
		for( let j = Math.floor(spacing/2); j < this.C.extents[1] ; j += spacing ){
			this.C.setpix( [i,j], this.C.makeNewCellID(2) )
			numberOfObstacles++
		}
	}
}

function initialize(){
	sim = new CPM.Simulation( config, {initializeGrid : initializeGrid} )
	meter = new FPSMeter({left:"auto", right:"5px"})
	step()
}

function step(){
	sim.step()
	meter.tick()
	requestAnimationFrame( step )
}



/****** Button functionality ******/

function startsim(){
	if( !sim.running ){
		sim.running = true
	}
}

function stopsim(){
	sim.running = false
}

function seedCell( k ){
	sim.gm.seedCell(k)
}

function seedCells( ncells ){
	for( let i = 0; i < ncells; i++ ){
		seedCell( 1 )
	}
}

function killCells( ncells ){
	let t
	let cells = Object.keys( sim.C.getStat( CPM.PixelsByCell ) )
	for ( let i = 0; i < ncells; i++ ){
		if( cells.length > 0 ){
			t = cells.pop()
			if( t > numberOfObstacles ){
				for( let cp of sim.C.cellPixels() ){
					if( cp[1] == t ){
						sim.C.setpix( cp[0], 0 )
					}
				}
			}
		}
	}
	sim.C.stat_values = {}
}