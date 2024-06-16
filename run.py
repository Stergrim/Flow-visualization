# run Запуск пользовательских визуализаций

import scipy.io
import argparse
import numpy as np
from matplotlib.colors import ListedColormap

from computeColor import visualComputeColor
from visualizationFlow import visualization_vector
from demonstration import demoTest
from demonstration import demoColormaps

# Параметры по умолчанию
parser = argparse.ArgumentParser(description="Inferencing script for visualization")
parser.add_argument("--flowfile", type=str, 
                    default="demos/vortexPair.flo",
                    help="Flow file")
parser.add_argument("--color", type=str, default='r', help="Choose the color of the vectors")
parser.add_argument("--step_x", type=int, default=16, help="Step between vectors on the x-axis")
parser.add_argument("--step_y", type=int, default=16, help="Step between vectors on the y-axis")
parser.add_argument("--size_vec", type=int, default=1, help="How many times to increase the size of the vectors")
parser.add_argument("--figsize_x", type=int, default=8, help="Picture size horizontally")
parser.add_argument("--figsize_y", type=int, default=8, help="Vertical size of the picture ")
parser.add_argument("--figure_dpi", type=int, default=80, help="Drawing dpi")
parser.add_argument("--background", type=str,
                    default="demos/vortexPair_img1.png",
                    help="Background file")
parser.add_argument("--colormaps", default=None, help="Choose a color maps")
parser.add_argument("--help_color", type=str, default=None, help="Standard color maps")

args = parser.parse_args()

# Определение пользовательских параметров
args.flowfile = "demos/DNS_turbulence.flo"
args.color = 'red'
args.step_x = 5
args.step_y = 5
args.size_vec = 5
args.figsize_x = 8
args.figsize_y = 8
args.figure_dpi = 80
args.background = "demos/DNS_turbulence_img1.png" # None
args.colormaps = None # 'RdYlBu_r'
args.help_color = None # "colormaps"

# Запуск визуализации
visualization_vector(args)

# Визуализация смещений через цветовой круг (не настраиваемая)
# visualComputeColor(args.flowfile)

# Демонстрация различных сценариев
# demoTest()
# Демонстрация цветовых карт
# demoColormaps()