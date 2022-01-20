import os

SRC_IMG_PATH = "./img_src/DIV2K_train_1080pHD"
TRG_IMG_PATH = "./img_src/encoded_train_1080pHD"

count = 0
filenames = [os.path.join(SRC_IMG_PATH, name) for name in os.listdir(SRC_IMG_PATH)]
for path in filenames:
    file_name = os.path.join(TRG_IMG_PATH, "{}.mp4".format(str(count).zfill(4)))
    count += 1
    os.system("ffmpeg -i {} -pix_fmt yuv420p {}".format(path, file_name))