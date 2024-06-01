import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

from readFlowFile import read_flow

def visualization_vector(args):

    if (args.flowfile == None):
        print("Не задан файл flow")
        return

    if (args.help_color == "colormaps"):
        colormaps_txt = [['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2'],
              ['Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r'],
              ['Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr'],
              ['PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r'],
              ['RdYlGn','RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia'],
              ['Wistia_r', 'YlGn','YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r'],
              ['binary', 'binary_r','bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm'],
              ['coolwarm_r', 'copper', 'copper_r','cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r'],
              ['gist_ncar','gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray'],
              ['gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r'],
              ['ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring'],
              ['spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r'],
              ['turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r', '' , '', '']]
        for x in colormaps_txt:
            print("{:13}{:14}{:15}{:17}{:19}{:21}{:12}{:14}{:15}{:12}{:14}{:16}{:17}".format(*x))
        return

    flo = read_flow(args.flowfile)

    Y, X = np.meshgrid(range(args.step_y, flo.shape[0], args.step_y), range(args.step_x, flo.shape[1], args.step_x))
    U, V = flo[Y, X].T

    all_points = np.array(list(zip(X.flatten(), Y.flatten())), dtype=float)

    X = [point[0] for point in all_points]
    Y = [point[1] for point in all_points]

    if ((args.background == None) & (args.colormaps == None)):
        plt.rcParams['figure.figsize'] = [args.figsize_x, args.figsize_y]
        plt.rcParams['figure.dpi'] = args.figure_dpi
        plt.quiver(X, Y, U.T, -V.T, color=args.color, scale=flo.shape[1]/args.size_vec)
        plt.gca().invert_yaxis()
        plt.show()
    elif ((args.background != None) & (args.colormaps == None)):
        plt.rcParams['figure.figsize'] = [args.figsize_x, args.figsize_y]
        plt.rcParams['figure.dpi'] = args.figure_dpi
        img = PIL.Image.open(args.background)
        plt.imshow(img)
        plt.quiver(X, Y, U.T, -V.T, color=args.color, scale=flo.shape[1]/args.size_vec)
        plt.show()
    elif ((args.background == None) & (args.colormaps != None)):
        norm_vec = np.zeros([flo.shape[0], flo.shape[1]])

        for i in range(flo.shape[0]):
            for j in range(flo.shape[1]):
                norm_vec[i,j] = np.sqrt(flo[i,j,0]*flo[i,j,0] + flo[i,j,1]*flo[i,j,1])

        # Выбор стандартная цветовая карта или кастомная
        if (type(args.colormaps) == str):
            colormaps = [args.colormaps] # стандратная
        else:
            colormaps = [args.colormaps] # кастомная

        n = len(colormaps)
        fig, axs = plt.subplots(1, n,figsize=(int((n*args.figsize_x + 2)/1.5), int(args.figsize_y/1.5)),
                                constrained_layout=True, squeeze=False)
        for [ax, cmap] in zip(axs.flat, colormaps):
            psm = ax.pcolormesh(norm_vec, cmap=cmap, rasterized=True)
            fig.colorbar(psm, ax=ax)
        
        plt.quiver(X, Y, U.T, -V.T, color=args.color, scale=flo.shape[1]/args.size_vec)
        plt.gca().invert_yaxis()
        plt.show()
    else:
        print( "Выбран и фон и карта цетов. Выберете что-то одно. args.background != None and args.colormaps != None")