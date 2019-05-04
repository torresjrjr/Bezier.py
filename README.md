# Bezier.py
Create Bezier curves in Python

## Preview plots with (matplotlib)[https://matplotlib.org/gallery/index.html]
![An assortment of Bezier curves plotted with matplotlib.pyplot](https://i.imgur.com/lAXdYWS.png)

_Here's a 14-point 3D Bezier curve:_  

![14 - point 3D Bezier curve](https://i.imgur.com/Yw2u2FX.gif)

## How to use
Save the main file Bezier.py into your local directory to import into your python code.
Import **Bezier** and **numpy** and use. Bezier only has 1 class for now, so you can use this code:

```Python
from Bezier import Bezier
import numpy as np
```
Create a Bezier curve with parameter `t` and an array of inital points `points1` of any dimension. Here's a 2D example:

```Python
t_points = np.arange(0, 1, 0.01)  # Creates an iterable list from 0 to 1.
points1 = np.array([[0, 0], [0, 8], [5, 10], [9, 7], [4, 3]])  # Creates an array of coordinates.
curve1 = Bezier.Curve(t_points, points1)		# Returns an array of coordinates.
```

You could plot your creations with matplotlib.

```Python
import matplotlib.pyplot as plt

plt.figure()
plt.plot(
	curve1[:, 0],   # x-coordinates.
	curve1[:, 1]    # y-coordinates.
)
plt.plot(
	points1[:, 0],  # x-coordinates.
	points1[:, 1],  # y-coordinates.
	'ro:'           # Styling.
)
plt.grid()
plt.show()
```
The result:

![The resulting plot](https://i.imgur.com/DWjxns7.png) 

## Dependancies
- Python
- numpy