import scipy.io
import argparse
import numpy as np
from matplotlib.colors import ListedColormap

from computeColor import visualComputeColor
from visualizationFlow import visualization_vector

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

# Общая демострация
def demoTest():
    print("Векторное поле на фоне изображения")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test/flow/vortexPair_img1_out.flo"
    args.color = 'red'
    args.step_x = 8
    args.step_y = 8
    args.size_vec = 5
    args.figsize_x = 8
    args.figsize_y = 8
    args.figure_dpi = 80
    args.background = "demo/test/vortexPair_img1.png"
    args.colormaps = None
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле на кастомной цветовой карте, которая аналогична стандартной: RdYlBu_r")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test/flow/vortexPair_img1_out.flo"
    args.color = 'black'
    args.step_x = 16
    args.step_y = 16
    args.size_vec = 5
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None

    # load colormaps 
    BuYlRd = np.array(scipy.io.loadmat("demo/colorMapsCustom/BuYlRd.mat")['BuYlRd'])

    # define colormaps 
    BuYlRdColors = ListedColormap(BuYlRd, name='BuYlRd')

    args.colormaps = BuYlRdColors
    args.help_color = None

    visualization_vector(args)

    print("Векторное поле на встроенной цветовой карте: Set1")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test/flow/vortexPair_img1_out.flo"
    args.color = 'black'
    args.step_x = 16
    args.step_y = 16
    args.size_vec = 5
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'Set1'
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для трёхцветной картинки")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/testColor/flow/one_out.flo"
    args.color = 'red'
    args.step_x = 8
    args.step_y = 8
    args.size_vec = 3
    args.figsize_x = 10
    args.figsize_y = 6
    args.figure_dpi = 80
    args.background = "demo/testColor/one.png"
    args.colormaps = None
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для трёхцветной картинки на цветовой карте")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/testColor/flow/one_out.flo"
    args.color = 'black'
    args.step_x = 16
    args.step_y = 16
    args.size_vec = 3
    args.figsize_x = 10
    args.figsize_y = 6
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Скрипт взятый с gitHub")
    visualComputeColor(args.flowfile)

    print("Векторное поле для test2")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test2/flow/backstep_Re1000_img1_out.flo"
    args.color = 'black'
    args.step_x = 8
    args.step_y = 8
    args.size_vec = 2
    args.figsize_x = 10
    args.figsize_y = 6
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для test3")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test3/flow/DNS_turbulence_img1_out.flo"
    args.color = 'black'
    args.step_x = 4
    args.step_y = 4
    args.size_vec = 3
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для test4")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test4/flow/As_twin_jet_1_out.flo"
    args.color = 'black'
    args.step_x = 8
    args.step_y = 8
    args.size_vec = 3
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для test5")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test5/flow/wall_jet_1_out.flo"
    args.color = 'black'
    args.step_x = 16
    args.step_y = 16
    args.size_vec = 3
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для test6")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test6/flow/White_Oval_1_out.flo"
    args.color = 'black'
    args.step_x = 8
    args.step_y = 8
    args.size_vec = 3
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для test7")
    print("Изображение деформированные с помощью dewarp")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test7/flow/RswarpImageImg1_out.flo"
    args.color = 'r'
    args.step_x = 16
    args.step_y = 16
    args.size_vec = 2
    args.figsize_x = 8
    args.figsize_y = 8
    args.figure_dpi = 80
    args.background = "demo/test7/RswarpImageImg1.jpg"
    args.colormaps = None
    args.help_color = None
    visualization_vector(args)

    print("Векторное поле для test7")
    print("Изображение деформированные с помощью dewarp")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test7/flow/RswarpImageImg1_out.flo"
    args.color = 'black'
    args.step_x = 16
    args.step_y = 16
    args.size_vec = 2
    args.figsize_x = 10
    args.figsize_y = 11
    args.figure_dpi = 80
    args.background = None
    args.colormaps = 'RdYlBu_r'
    args.help_color = None
    visualization_vector(args)

    print("Список всех встроенных цветовых карт:")
    args.help_color = "colormaps"
    visualization_vector(args)


# Демонстрация некоторых цветовых палитр
def demoColormaps():
    print("Демострация некоторых отобранных цветовых карт: 9 штук")
    args.flowfile = "demo/result/PIV-LiteFlowNet-en/test/flow/vortexPair_img1_out.flo"
    args.color = 'black'
    args.step_x = 32
    args.step_y = 32
    args.size_vec = 1
    args.figsize_x = 10
    args.figsize_y = 10
    args.figure_dpi = 80
    args.background = None
    args.help_color = None

    txt = [['RdYlBu_r', 'Spectral_r', 'tab10_r', 'CMRmap', 'Greys', 'Greys_r'],
        ['OrRd', 'PuOr_r', 'RdBu_r', 'RdGy_r', 'afmhot', 'binary'],
        ['binary_r', 'bwr', 'coolwarm', 'gist_gray', 'gist_gray_r', 'gist_heat'],
        ['gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_yarg'],
        ['gist_yarg_r', 'gnuplot', 'gnuplot2', 'gray', 'gray_r', 'inferno'],
        ['jet', 'nipy_spectral', 'plasma', 'rainbow', 'turbo', '']]

    example = [ 'RdYlBu_r', 'Spectral_r', 'tab10_r', 'CMRmap', 'Greys', 'Greys_r', 'coolwarm', 'gnuplot2', 'turbo']

    for e in example:
        args.colormaps = e
        print("Цветовая палитра: " + e)
        visualization_vector(args)

    print("Отобранные цветовые карты:")
    for x in txt:
        print("{:14}{:16}{:16}{:17}{:14}{:12}".format(*x))
