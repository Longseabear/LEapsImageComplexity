import matplotlib.pyplot as plt
from PIL import Image
import path
import os
import numpy as np

class ImageSaver:
    def __init__(self, output_folder, renumbering=False):
        self.name = "print task"
        self.output_folder = output_folder
        self.count = 0
        self.renumbering = renumbering

    def run(self, img, info):
        if self.renumbering:
            file_name = "{}.png".format(str(self.count).zfill(4))
            self.count += 1
        else:
            file_name = os.path.basename(info['filename'])
        save_path = os.path.join(self.output_folder, file_name)
        result = Image.fromarray(img)
        result.save(save_path)
        return img, info

class ImageResolutionPrint:
    def __init__(self):
        self.name = "print task"

    def run(self, img, info):
        print(img.shape, info)
        return img, info

class Rescale:
    def __init__(self, mode = '1920x1080'):
        self.name = "Rescale {}".format(mode)
        self.mode = mode
        self.th = None
        self.tw = None

    def rescale_1080pHDWide(self, img, info):
        h, w, c = img.shape

        #setting
        if h > w:
            self.th = 1920
            self.tw = 1088
        else:
            self.th = 1088
            self.tw = 1920

        if h < self.th or w < self.tw:
            raise Exception('target resolution missmatching')

        sh = h // 2 - (self.th // 2)
        sw = w // 2 - (self.tw // 2)

        img = img[sh: sh+self.th, sw:sw+self.tw]
        return img, info


    def run(self, img, info):
        if self.mode == '1920x1080':
            return self.rescale_1080pHDWide(img, info)
        return False