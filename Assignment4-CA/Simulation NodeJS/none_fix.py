import matplotlib.image as mpimg
import os

directory = './output/'

for folder in os.listdir(directory):
    if 'None' not in folder and not '.DS_Store' in folder:
        for image_name in os.listdir(directory+folder+"/"):
            if image_name.endswith('00.png') and not image_name.startswith('WITH_LINE'):
                img = mpimg.imread(directory+folder+"/"+image_name)
                img[:, -201:-199] = 0.
                mpimg.imsave(directory+folder+"/WITH_LINE"+image_name, img)