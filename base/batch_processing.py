import matplotlib.pyplot as plt
from PIL import Image
import path
import os
import numpy as np
from batch_tasks import *

class BatchProcess:
    def __init__(self, folder_path, task, exp='png'):
        self.dirs = [os.path.join(folder_path, file_name) for file_name
                     in os.listdir(folder_path)]
        self.tasks = task

    def run(self):
        for path in self.dirs:
            img = Image.open(path)
            info = img.__dict__
            img = np.array(img)
            # dict_keys(['im', 'mode', '_size', 'palette', 'info', 'category', 'readonly', 'pyaccess', '_exif', '_min_frame', 'custom_mimetype', 'tile', 'decoderconfig', 'decodermaxblock', 'fp', 'filename', '_exclusive_fp', '_PngImageFile__fp', '_PngImageFile__frame', 'png', '_text', 'n_frames', 'default_image', '_PngImageFile__prepare_idat', 'is_animated', 'map', '_PngImageFile__idat'])
            print(info['filename'], os.path.basename(info['filename']))
            try:
                for task_obj in self.tasks:
                    img, info = task_obj.run(img, info)
            except Exception as e:
                print("fail: ", e, task_obj.name, info)

# batch = BatchProcess('img_src/DIV2K_train_HR', [Rescale(), ImageResolutionPrint(),
#                                                 ImageSaver('img_src/DIV2K_train_1080pHD', True)])
batch = BatchProcess('img_src/DIV2K_train_1080pHD', [AddIntraBitRate('img_src/encoded_train_1080pHD')])

batch.run()
