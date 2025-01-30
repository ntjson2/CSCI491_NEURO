import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from scipy.spatial import ConvexHull

def rounded_cube(radius=0.1, resolution=10):
    # Create a grid of points
    u = np.linspace(0, 1, resolution)
    v = np.linspace(0, 1, resolution)
    w = np.linspace(0, 1, resolution)
    u, v, w = np.meshgrid(u, v, w)
    u, v, w = u.flatten(), v.flatten(), w.flatten()

    # Create the vertices of the rounded cube
    vertices = np.vstack([u, v, w]).T
    vertices = vertices * (1 - 2 * radius) + radius

    # Create the faces of the rounded cube
    faces = ConvexHull(vertices).simplices

    return vertices, faces

# Generate the rounded cube
vertices, faces = rounded_cube()

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the faces of the rounded cube
for face in faces:
    ax.add_collection3d(Poly3DCollection([vertices[face]], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Set the limits of the plot
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()