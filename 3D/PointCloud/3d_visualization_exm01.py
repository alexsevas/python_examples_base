# conda create -n 3dpy39 tensorflow numpy==1.23.4 python=3.9 -y
# conda activate 3dpy39
# pip install retina-face
# pip install laspy
# pip install open3d


import numpy as np
import laspy
import open3d as o3d

las = laspy.read('NZ19_Wellington.las')
list(las.point_format.dimension_names)
set(list(las.classification))

point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)

o3d.visualization.draw_geometries([geom])
