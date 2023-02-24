from sklearn.utils import Bunch
from sklearn.neighbors import KNeighborsClassifier
import cv2
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

class Dataset:
    
    def show_ratios_distributions(self):
        ratios = list()
        for i in tqdm(self.images):
            ratios.append(i.shape[1] / i.shape[0]) # x / y

        fig, axs = plt.subplots(1, 1,  tight_layout=True)

        # We can set the number of bins with the *bins* keyword argument.
        axs.hist(ratios)
        plt.title('distributions of width / height ratios')
        plt.show()
    def resize_all(self):
        print('resizing images to height %d ...' % (self.common_dimensions[0]))
        for i in tqdm(range(len(self.images))):
            height = int(self.common_dimensions[0])
            width = int(self.images[i].shape[1] * ( self.common_dimensions[0] / self.images[i].shape[1]))
            self.images[i] = cv2.resize(self.images[i], (width, height))
            print('Resized Dimensions : ', self.images[i].shape)
            plt.imshow(self.images[i])  
            plt.title(self.titles[i])
            plt.show()

            
    def __init__(self, path):
        dir_contents = os.listdir(path)
        self.images = list()
        self.titles = list()

        smallest_height = 10000000
        smallest_width = 10000000

        vertical_avoided = 0
        too_small_avoided = 0

        # in this loop, we retain landscape pictures with a min width of 500
        # and retain the highest dimension that can be commonly retained for all the dataset
        for file in tqdm(dir_contents):
            if file.endswith('.jpeg') == False:
                continue
            contents = cv2.imread(os.path.join(path, file), cv2.IMREAD_GRAYSCALE)

            # si height > width ou si width < 500
            if contents.shape[0] > contents.shape[1]:
                vertical_avoided += 1
                continue
            if contents.shape[0] < 500:
                too_small_avoided += 1
                continue

            # (y / x, (y, x))
            current_dimensions = (contents.shape[0], contents.shape[1])
            self.images.append(contents)
            self.titles.append(file)
            if smallest_height > current_dimensions[0]:
                smallest_height = current_dimensions[0]
            if smallest_width > current_dimensions[1]:
                smallest_width = current_dimensions[1]
            # print('%s\t\t %d x %d' % (file, current_dimensions[1], current_dimensions[0])
        self.common_dimensions = (smallest_height, smallest_width)
        print('vertical_avoided = %d' % (vertical_avoided))
        print('too_small_avoided = %d' % (too_small_avoided))
        print('common_dimensions = y %d x %d' % (smallest_height, smallest_width))    

base_path="./dataset"

train_pneumonia = Dataset(base_path + '/train/PNEUMONIA')
train_pneumonia.show_ratios_distributions()
train_pneumonia.resize_all()
#train_normal =  gather_ratios(base_path + '/train/NORMAL')
#test_pneumonia =  gather_ratios(base_path + '/test/PNEUMONIA')
#test_normal =  gather_ratios(base_path + '/test/NORMAL')