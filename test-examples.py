from Bezier import Bezier
import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#~~~#

fig = plt.figure(dpi=128)

#~~~# 3D "Clockwise helix and drop"

points_set_1 = a([[0, 0, 0], [0, 4, 0], [2, 5, 0], [4, 5, 0], [5, 4, 0], [5, 1, 0], [4, 0, 0], [1, 0, 3], [0, 0, 4], [0, 2, 5], [0, 4, 5], [4, 5, 5], [5, 5, 4], [5, 5, 0]])
t_points = np.arange(0, 1, 0.01)
curve_set_1 = Bezier.Curve(t_points, points_set_1)

ax = fig.add_subplot(111, projection='3d')
ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2])
ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

#~~~#

plt.show()

help(Bezier)
