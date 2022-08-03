import argparse
import numpy as np
import os
from PIL import Image
from matplotlib import image


# NUM_CHANNELS = 3
# TODO: decide how this is calculated?
WIDTH = 1500
HEIGHT = 2000

def np_to_bin(arr, out):
    if os.path.exists(out):
        os.remove(out)
    with open(out, "wb") as fid:
        h, w, c = arr.shape
        fid.write(bytes(f"{w}&{h}&{c}&", 'utf-8'))
        
        arr = arr.astype(np.float32)
        arr = np.transpose(arr, (1, 0, 2)).squeeze()
        fid.write(arr.tobytes(order='F'))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="path to source image", type=str, required=True)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    if not os.path.exists(args.source):
        raise FileNotFoundError("File not found: {}".format(args.source))

    img = Image.open(args.source)
    img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    img = np.asarray(img)    

    # import pylab as plt

    # print(img.shape)
    # plt.figure()
    # plt.imshow(img)
    # plt.title('depth map')

    # plt.show()

    np_to_bin(img / 255, f"{args.source}.bin")

if __name__ == "__main__":
    main()
