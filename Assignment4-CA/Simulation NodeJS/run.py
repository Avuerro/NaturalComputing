import os

nrCells = 10
for spacing in [25,31,50,83,9999999]:
    for i in range(1,11):
        folder_name = f"output/{nrCells}-{'None' if spacing==9999999 else spacing}-{i}"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        os.popen(f"node simulation_nodejs.js keratocyte {spacing} {nrCells} 10000 {i} {folder_name}")