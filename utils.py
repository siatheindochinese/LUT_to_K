import numpy as np

def pixAndRay(lut):
	height, width = lut.shape[0], lut.shape[1]
	x = np.linspace(0, width-1, width)
	y = np.linspace(0, height-1, height)
	xx, yy = np.meshgrid(x, y)
	xx = xx.reshape(1,-1).astype(int)
	yy = yy.reshape(1,-1).astype(int)
	coords_2d = np.concatenate([xx, yy,np.ones((1,height*width))], axis=0).astype(int).T
	rays_3d = lut[yy.reshape(-1),xx.reshape(-1)]
	return coords_2d.T, rays_3d.T

