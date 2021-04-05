import matplotlib.image as mpimg
import os

directory = './output/'

for folder in os.listdir(directory):
    if not os.path.exists(directory+folder+"/IMPORTANT"):
        os.mkdir(directory+folder+"/IMPORTANT")
    for image_name in os.listdir(directory+folder+"/"):
        if image_name.endswith('99.png'):
            img = mpimg.imread(directory+folder+"/"+image_name)
            img[:, -201:-199] = 0.
            mpimg.imsave(directory+folder+"/IMPORTANT/"+image_name, img)