# readFlowFile читает файл flow (.flo) и записывает в 3-ех мерный массив, где
# компонеты векторного поля записаны следющим образом:
# U = flow(:,:,1)
# V = flow(:,:,2)

######################################################################
# According to the c++ source code of Daniel Scharstein
# Contact: schar@middlebury.edu

# Author: Deqing Sun, Department of Computer Science, Brown University
# Contact: dqsun@cs.brown.edu
# Date: 2007-10-31 16:45:40 (Wed, 31 Oct 2006)
######################################################################

import os
import numpy as np

# Проверка первых байтов файла (0-3 байта).
# Тег: "PIEH" в ASCII, который в строчном порядке оказывается
# значением с плавающей точкой 202021.25
# (просто проверка правильности представления значений с плавающей точкой)
TAG_FLOAT = 202021.25

def read_flow(file):
    assert type(file) is str, "file is not str %r" % str(file)
    assert os.path.isfile(file) is True, "file does not exist %r" % str(file)
    assert file[-4:] == '.flo', "file ending is not .flo %r" % file[-4:]
    f = open(file,'rb')
    flo_number = np.fromfile(f, np.float32, count=1)[0]
    assert flo_number == TAG_FLOAT, 'Flow number %r incorrect. Invalid .flo file' % flo_number
    w, h = np.fromfile(f, np.int32, count=2)
    #if error try: data = np.fromfile(f, np.float32, count=2*w[0]*h[0])
    data = np.fromfile(f, np.float32, count=2*w*h)
    # Reshape data into 3D array (columns, rows, bands)
    flow = np.resize(data, (int(h), int(w), 2))
    f.close()

    return flow