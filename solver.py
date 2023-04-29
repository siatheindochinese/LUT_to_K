import numpy as np

def leastSquares(coords_2d, rays_3d):
	A = (rays_3d / rays_3d[2]).T
	Ax = A[:,[0,2]]
	Ay = A[:,[1,2]]
	
	b = (coords_2d / coords_2d[2]).T
	bx = b[:,0]
	by = b[:,1]
	
	# solve for fx and cx
	fx, cx = np.linalg.inv(Ax.T @ Ax) @ Ax.T @ bx
	# solve for fy and cy
	fy, cy = np.linalg.inv(Ax.T @ Ax) @ Ax.T @ bx
	
	K = np.eye(3)
	K[0,0], K[1,1], K[0,2], K[1,2] = fx, fy, cx, cy
	
	return K
	
def leastSquaresAlt(coords_2d, rays_3d):
	A = (rays_3d / rays_3d[2]).T
	Ax = A[:,[0,2]]
	Ay = A[:,[1,2]]
	
	b = (coords_2d / coords_2d[2]).T
	bx = b[:,0]
	by = b[:,1]
	
	# solve for fx and cx
	fx, cx = np.linalg.lstsq(Ax, bx, rcond=-1)[0]
	# solve for fy and cy
	fy, cy = np.linalg.lstsq(Ay, by, rcond=-1)[0]
	
	K = np.eye(3)
	K[0,0], K[1,1], K[0,2], K[1,2] = fx, fy, cx, cy
	
	return K
	
