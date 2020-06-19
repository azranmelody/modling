#load several images from file
import os
from matplotlib import image

def load_several_imgs(path , only_few_number='all'):
    images_files_names = os.listdir(path)
    
    data = []
    if(only_few_number=='all'):
        how_many_images = len(images_files_names)
    else:
        how_many_images = only_few_number
    
    for i in range(how_many_images):
        data.append(image.imread(path + '/' + images_files_names[i]))
        
    return data