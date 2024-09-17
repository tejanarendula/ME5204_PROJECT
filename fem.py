import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
num_nodes = 8
num_elements = 6 #cst element
num_materials = 2
problem_type = 21 #plane stress
thickness = 0.5
num_load_bc = 2 #number of lolads applied
num_disp_bc = 2 #number of places displacement condition is applied
COORD = np.loadtxt(fname = 'D:\\SAI TEJA\\DATA\\COORD.txt').astype(np.float32)
NCA = np.loadtxt(fname = 'D:\\SAI TEJA\\DATA\\NCA.txt').astype(np.int32)
MAT = np.loadtxt(fname = 'D:\SAI TEJA\DATA\MAT.txt').astype(np.float32)
LOAD_BC = np.loadtxt(fname = 'D:\SAI TEJA\DATA\LOAD_BC.txt').astype(np.float32)
DISP_BC = np.loadtxt(fname = 'D:\SAI TEJA\DATA\DISP_BC.txt').astype(np.float32)
for ele in range(1, num_elements + 1, 1):

    # ----Extraction of Nodes-----

    N1 = NCA[ele, 1]
    N2 = NCA[ele, 2]
    N3 = NCA[ele, 3]

    # ----Extraction of Nodal Co-ordinates----

    X1N1 = COORD[N1, 1]
    X2N1 = COORD[N1, 2]
    X1N2 = COORD[N2, 1]
    X2N2 = COORD[N2, 2]
    X1N3 = COORD[N3, 1]
    X2N3 = COORD[N3, 2]

    # -----Extraction of Material Type of Element----

    Mat_num = NCA[ele, 4]

    # -----Plotting the model of given problem----

    X = [X1N1, X1N2, X1N3]
    Y = [X2N1, X2N2, X2N3]
    CGX = (X1N1 + X1N2 + X1N3) / 3
    CGY = (X2N1 + X2N2 + X2N3) / 3
    if Mat_num == 1:
        plt.fill(X, Y, 'y')
    else:
        plt.fill(X, Y, 'b')
    plt.scatter(X, Y, c='black')
    plt.text(CGX, CGY, str(ele))
    plt.show



