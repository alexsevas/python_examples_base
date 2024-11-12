# conda create -n 3dpy39 tensorflow numpy==1.23.4 python=3.9 -y
# conda activate 3dpy39
# pip install retina-face
# pip install laspy
# pip install open3d

# [Open3D INFO]   -- Mouse view control --
# [Open3D INFO]     Left button + drag         : Rotate.
# [Open3D INFO]     Ctrl + left button + drag  : Translate.
# [Open3D INFO]     Wheel button + drag        : Translate.
# [Open3D INFO]     Shift + left button + drag : Roll.
# [Open3D INFO]     Wheel                      : Zoom in/out.
# [Open3D INFO]
# [Open3D INFO]   -- Keyboard view control --
# [Open3D INFO]     [/]          : Increase/decrease field of view.
# [Open3D INFO]     R            : Reset view point.
# [Open3D INFO]     Ctrl/Cmd + C : Copy current view status into the clipboard.
# [Open3D INFO]     Ctrl/Cmd + V : Paste view status from clipboard.
# [Open3D INFO]
# [Open3D INFO]   -- General control --
# [Open3D INFO]     Q, Esc       : Exit window.
# [Open3D INFO]     H            : Print help message.
# [Open3D INFO]     P, PrtScn    : Take a screen capture.
# [Open3D INFO]     D            : Take a depth capture.
# [Open3D INFO]     O            : Take a capture of current rendering settings.
# [Open3D INFO]     Alt + Enter  : Toggle between full screen and windowed mode.
# [Open3D INFO]
# [Open3D INFO]   -- Render mode control --
# [Open3D INFO]     L            : Turn on/off lighting.
# [Open3D INFO]     +/-          : Increase/decrease point size.
# [Open3D INFO]     Ctrl + +/-   : Increase/decrease width of geometry::LineSet.
# [Open3D INFO]     N            : Turn on/off point cloud normal rendering.
# [Open3D INFO]     S            : Toggle between mesh flat shading and smooth shading.
# [Open3D INFO]     W            : Turn on/off mesh wireframe.
# [Open3D INFO]     B            : Turn on/off back face rendering.
# [Open3D INFO]     I            : Turn on/off image zoom in interpolation.
# [Open3D INFO]     T            : Toggle among image render:
# [Open3D INFO]                    no stretch / keep ratio / freely stretch.
# [Open3D INFO]
# [Open3D INFO]   -- Color control --
# [Open3D INFO]     0..4,9       : Set point cloud color option.
# [Open3D INFO]                    0 - Default behavior, render point color.
# [Open3D INFO]                    1 - Render point color.
# [Open3D INFO]                    2 - x coordinate as color.
# [Open3D INFO]                    3 - y coordinate as color.
# [Open3D INFO]                    4 - z coordinate as color.
# [Open3D INFO]                    9 - normal as color.
# [Open3D INFO]     Ctrl + 0..4,9: Set mesh color option.
# [Open3D INFO]                    0 - Default behavior, render uniform gray color.
# [Open3D INFO]                    1 - Render point color.
# [Open3D INFO]                    2 - x coordinate as color.
# [Open3D INFO]                    3 - y coordinate as color.
# [Open3D INFO]                    4 - z coordinate as color.
# [Open3D INFO]                    9 - normal as color.
# [Open3D INFO]     Shift + 0..4 : Color map options.
# [Open3D INFO]                    0 - Gray scale color.
# [Open3D INFO]                    1 - JET color map.
# [Open3D INFO]                    2 - SUMMER color map.
# [Open3D INFO]                    3 - WINTER color map.
# [Open3D INFO]                    4 - HOT color map.
# [Open3D INFO]

import numpy as np
import laspy
import open3d as o3d

las = laspy.read('2020_Drone_M.las')
list(las.point_format.dimension_names)
set(list(las.classification))

point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1, 0))

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)

o3d.visualization.draw_geometries([geom])
