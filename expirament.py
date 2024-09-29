import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the triangle
x1 = np.array([0, 1, 2])
y1 = np.array([0, 2, 1])
z1 = np.array([0, 0, 2])

# Create the figure and add a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a collection of triangles from the vertices
verts = [list(zip(x1, y1, z1))]
triangles = Poly3DCollection(verts)

# Set the color of the triangle
triangles.set_color('red')

# Add the triangle to the subplot
ax.add_collection(triangles)

# Set the limits of the plot
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

# Show the plot
plt.show()