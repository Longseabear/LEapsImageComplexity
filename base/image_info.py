import matplotlib.pyplot as plt
from PIL import Image
import path
import os

class ImageInfos:
    def __init__(self, folder_path, exp='png'):
        self.dirs = [os.path.join(folder_path, file_name) for file_name
                     in os.listdir(folder_path)]

    def show(self):
        for path in self.dirs:
            img = Image.open(path)
            print(img)
            print(img.__dict__)
image_info = ImageInfos('img_src/DIV2K_train_HR')
image_info.show()