from Bezier import Bezier
import numpy as np
from numpy import array as a
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#~~~#

fig = plt.figure(dpi=128)

#~~~# Simple arch.

t_points = np.arange(0, 1, 0.01)
test = a([[0, 0], [0, 8], [5, 10], [9, 7], [4, 3]])
test_set_1 = Bezier.Curve(t_points, test)

plt.subplot(2, 3, 3)
plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

plt.plot(test_set_1[:, 0], test_set_1[:, 1])
plt.plot(test[:, 0], test[:, 1], 'ro:')

#~~~# Simple wave.

t_points = np.arange(0, 1, 0.01)
test = a([[0, 5], [4, 10], [6, 10], [4, 0], [6, 0], [10, 5]])
test_set_1 = Bezier.Curve(t_points, test)

plt.subplot(2, 3, 6)
plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

plt.plot(test_set_1[:, 0], test_set_1[:, 1])
plt.plot(test[:, 0], test[:, 1], 'ro:')

#~~~# Plushy heart.

points2 = a([[5, 0], [0, 2], [0, 10], [6, 10], [14, -2], [-4, -2], [4, 10], [10, 10], [10, 2], [5, 0]])
t_points = np.arange(0, 1, 0.01)
curve2 = Bezier.Curve(t_points, points2)

plt.subplot(2, 3, 2)
plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

plt.plot(curve2[:, 0], curve2[:, 1], 'r')
plt.plot(points2[:, 0], points2[:, 1], 'yx:')

#~~~# 10-point Bezier curve.

points2 = a([[0, 2], [2, 8], [6, 6], [4, 4], [2, 2], [6, 0], [8, 4], [10, 8], [8, 10], [6, 9]])
t_points = np.arange(0, 1, 0.01)
curve2 = Bezier.Curve(t_points, points2)

plt.subplot(2, 3, 1)
plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')

plt.plot(curve2[:, 0], curve2[:, 1])
plt.plot(points2[:, 0], points2[:, 1], 'ro:')

#~~~# 3 of 3-point Bezier curves

points_set_1 = a([[0, 2], [2, 8], [6, 6], [4, 4]])
points_set_2 = a([[4, 4], [2, 2], [6, 0], [8, 4]])
points_set_3 = a([[8, 4], [10, 8], [8, 10], [6, 9]])

t_points = np.arange(0, 1, 0.01)

curve_set_1 = Bezier.Curve(t_points, points_set_1)
curve_set_2 = Bezier.Curve(t_points, points_set_2)
curve_set_3 = Bezier.Curve(t_points, points_set_3)

plt.subplot(2, 3, 4)
plt.xticks([i1 for i1 in range(-20, 20)]), plt.yticks([i1 for i1 in range(-20, 20)])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(b=True, which='major', axis='both')


plt.plot(curve_set_1[:, 0], curve_set_1[:, 1])
plt.plot(points_set_1[:, 0], points_set_1[:, 1], 'bs:')

plt.plot(curve_set_2[:, 0], curve_set_2[:, 1])
plt.plot(points_set_2[:, 0], points_set_2[:, 1], 'ro:')

plt.plot(curve_set_3[:, 0], curve_set_3[:, 1])
plt.plot(points_set_3[:, 0], points_set_3[:, 1], 'gx:')

#~~~# 3D "Clockwise helix and drop"

points_set_1 = a([[0, 0, 0], [0, 4, 0], [2, 5, 0], [4, 5, 0], [5, 4, 0], [5, 1, 0], [4, 0, 0], [1, 0, 3], [0, 0, 4], [0, 2, 5], [0, 4, 5], [4, 5, 5], [5, 5, 4], [5, 5, 0]])
t_points = np.arange(0, 1, 0.01)
curve_set_1 = Bezier.Curve(t_points, points_set_1)

ax = fig.add_subplot(235, projection='3d')
ax.plot(curve_set_1[:, 0], curve_set_1[:, 1], curve_set_1[:, 2])
ax.plot(points_set_1[:, 0], points_set_1[:, 1], points_set_1[:, 2], 'o:')

#~~~#

plt.show()

help(Bezier)
