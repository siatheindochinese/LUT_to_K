import numpy as np

def get_PS3EYE():
	K = np.loadtxt('K/ps3eye.txt')
	Kinv = np.linalg.inv(K)
	
	height, width = 480, 640
	x = np.linspace(0, width-1, width)
	y = np.linspace(0, height-1, height)
	xx, yy = np.meshgrid(x, y)
	xx = xx.reshape(1,-1).astype(int)
	yy = yy.reshape(1,-1).astype(int)
	coords_2d = np.concatenate([xx, yy,np.ones((1,height*width))], axis=0).astype(int)
	rays_3d = Kinv @ coords_2d
	rays_3d = rays_3d / np.linalg.norm(rays_3d, axis = 0)
	
	lut = np.zeros((height, width, 3))
	lut[yy.reshape(-1),xx.reshape(-1)] = rays_3d.T
	
	return lut
	
def GT():
	return np.loadtxt('K/ps3eye.txt')
