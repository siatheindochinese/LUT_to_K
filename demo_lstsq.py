import numpy as np
import matplotlib.pyplot as plt

from solver import leastSquares

from utils import pixAndRay
	
def sanityCheck(lut):
	import open3d as o3d
	from itertools import combinations
	height, width, _ = lut.shape
	print(height, width)
	origin = np.zeros(3)
	
	upperleft = lut[0,0] / lut[0,0,2]
	upperight = lut[0,width-1] / lut[0,width-1,2]
	lowerleft = lut[height-1,0] / lut[height-1,0,2]
	loweright = lut[height-1,width-1] / lut[height-1,width-1,2]
	
	points = np.array([origin,upperleft,upperight,lowerleft,loweright])
	lines = [*combinations([0,1,2,3,4],2)]
	
	line_set = o3d.geometry.LineSet()
	line_set.points = o3d.utility.Vector3dVector(points)
	line_set.lines = o3d.utility.Vector2iVector(lines)
	
	axis_set = o3d.geometry.LineSet()
	zdir = np.array([0,0,1])
	ydir = np.array([0,1,0])
	xdir = np.array([1,0,0])
	
	axes = np.row_stack([np.zeros(3),np.linspace(1,3,3)]).astype(int).T
	axis_set.points = o3d.utility.Vector3dVector([origin,xdir,ydir,zdir])
	axis_set.lines = o3d.utility.Vector2iVector(axes)
	# x: red y: green z: blue
	axis_set.colors = o3d.utility.Vector3dVector([[1,0,0],[0,1,0],[0,0,1]])
	o3d.visualization.draw_geometries([line_set, axis_set])

if __name__ == '__main__':
	print('##########################')
	print('DEMO: Intel RealSense D455')
	print('##########################')
	from dataset.realsense import get_RS, GT
	lut = get_RS()
	#sanityCheck(lut)
	
	coords_2d, rays_3d = pixAndRay(lut)
	K_approx = leastSquares(coords_2d, rays_3d)
	print('ground-truth from RealSense API')
	print(GT())
	print('least-squares approximation')
	print(K_approx)
	
	print('')
	
	print('###################')
	print('DEMO: PS3EYE Camera')
	print('###################')
	from dataset.ps3eye import get_PS3EYE, GT
	lut = get_RS()
	#sanityCheck(lut)
	
	coords_2d, rays_3d = pixAndRay(lut)
	K_approx = leastSquares(coords_2d, rays_3d)
	print('ground-truth from chessboard camera calibration')
	print(GT())
	print('least-squares approximation')
	print(K_approx)
	
	print('')
	
	print('#############################################')
	print('DEMO: HoloLens2 VLC Cameras (no ground-truth)')
	print('#############################################')
	from dataset.hololens2 import get_LF, get_RF
	lut = get_LF()
	#sanityCheck(lut)
	
	coords_2d, rays_3d = pixAndRay(lut)
	print('least-squares approximation (LF)')
	K_approx = leastSquares(coords_2d, rays_3d)
	print(K_approx)
	lut = get_RF()
	#sanityCheck(lut)
	
	coords_2d, rays_3d = pixAndRay(lut)
	print('least-squares approximation (RF)')
	K_approx = leastSquares(coords_2d, rays_3d)
	print(K_approx)
	
