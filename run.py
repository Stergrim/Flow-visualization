import scipy.io
import argparse
import numpy as np
from matplotlib.colors import ListedColormap

from computeColor import visualComputeColor
from visualizationFlow import visualization_vector
from demonstration import demoTest
from demonstration import demoColormaps

parser = argparse.ArgumentParser(description="Inferencing script for visualization")
parser.add_argument("--flowfile", type=str, 
                    default="demo/result/PIV-LiteFlowNet-en/test/flow/vortexPair_img1_out.flo",
                    help="Flow file")
parser.add_argument("--color", type=str, default='r', help="Choose the color of the vectors")
parser.add_argument("--step_x", type=int, default=16, help="Step between vectors on the x-axis")
parser.add_argument("--step_y", type=int, default=16, help="Step between vectors on the y-axis")
parser.add_argument("--size_vec", type=int, default=1, help="How many times to increase the size of the vectors")
parser.add_argument("--figsize_x", type=int, default=8, help="Picture size horizontally")
parser.add_argument("--figsize_y", type=int, default=8, help="Vertical size of the picture ")
parser.add_argument("--figure_dpi", type=int, default=80, help="Drawing dpi")
parser.add_argument("--background", type=str,
                    default="demo/test/vortexPair_img1.png",
                    help="Background file")
parser.add_argument("--colormaps", default=None, help="Choose a color maps")
parser.add_argument("--help_color", type=str, default=None, help="Standard color maps")

args = parser.parse_args()

#args.flowfile = None
args.color = 'r'
args.step_x = 8
args.step_y = 8
args.size_vec = 5
args.figsize_x = 8
args.figsize_y = 8
args.figure_dpi = 80
args.background = None
args.colormaps = None # 'RdYlBu_r'
args.help_color = None # "colormaps"

#visualization_vector(args)

# Демонстрация
demoTest()
demoColormaps()