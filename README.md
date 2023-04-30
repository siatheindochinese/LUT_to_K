# LUT_to_K
Recover a camera intrinsic matrix (K) from a corresponding lookup table (LUT) through numerical optimization.

## To-Do List
- [x] Load LUT from `.bin` files
- [x] Generate LUT from K
- [x] Generate pixel-ray correspondences
- [x] Formulate problem statement
- [x] Implement naive solution
- [X] LUT sanity check
- [ ] Random K generator
- [ ] Implement numerical solutions
- [ ] Optional: recover distortion coefficients

## 1 Problem Statement

Certain AR/MR devices do not provide intrinsic values directly for their cameras. Instead, high-level functions exist to project 3D points to their corresponding 2D pixels and backproject 2D pixels to their corresponding rays (e.g. HoloLens2 Research Mode API has `MapImagePointToCameraUnitPlane` and `MapImagePointToCameraUnitPlane`).

Most popular computer vision libraries (e.g. OpenCV) require a 3x3 intrinsic matrix for their functions. Rewriting these functions to accomodate the high-level 2D-3D mapping functions from the aforementioned devices is an extremely tedious task.

We intend to recover these intrinsic parameters by sampling pixel-ray correspondences obtained from these high-level functions and using them to solve for the 4 intrinsic parameters $f_x$, $f_y$, $c_x$ and $c_y$.

Ultimately, this problem can be formulated as two systems of linear equations $Ax = b$ as follows:

$$
         u_{i}
     =
     \begin{bmatrix}
     	\frac{X_{i}}{Z_{i}} & 1
     \end{bmatrix}
     \begin{bmatrix}
     	f_{x} \\\ c_{x}
     \end{bmatrix}
     \text{ and }
     	v_{i}
     =
     \begin{bmatrix}
     	\frac{Y_{i}}{Z_{i}} & 1
     \end{bmatrix}
     \begin{bmatrix}
     	f_{y} \\\ c_{y}
     \end{bmatrix}
     \text{ for }
     i = 1, \cdots,wh
  $$

where $[u_{i}, v_{i}]^T$ are pixel coordinates, $[X_{i}, Y_{i}, Z_{i}]^T$ are the corresponding rays and $w$ and $h$ are the width and height of the LUT.

In theory, only 2 pixel-ray correspondences are needed to solve for all 4 intrinsic parameters. We may choose to use all pixel-ray correspondences from a LUT, resulting in two overdetermined systems of linear equations.

$$
     \begin{bmatrix}
     	u_{1} \\\ u_{2} \\\ \vdots \\\ u_{n}
     \end{bmatrix}
     =
     \begin{bmatrix}
     	\frac{X_{1}}{Z_{1}} & 1 \\\ \frac{X_{2}}{Z_{2}} & 1 \\\ \vdots \\\ \frac{X_{n}}{Z_{n}} & 1
     \end{bmatrix}
     \begin{bmatrix}
     	f_{x} \\\ c_{x}
     \end{bmatrix}
     \text{ and }
     \begin{bmatrix}
     	v_{1} \\\ v_{2} \\\ \vdots \\\ v_{n}
     \end{bmatrix}
     =
     \begin{bmatrix}
     	\frac{Y_{1}}{Z_{1}} & 1 \\\ \frac{Y_{2}}{Z_{2}} & 1 \\\ \vdots \\\ \frac{Y_{n}}{Z_{n}} & 1
     \end{bmatrix}
     \begin{bmatrix}
     	f_{y} \\\ c_{y}
     \end{bmatrix}
  $$
  
The first system of linear equations can be solved to obtain $f_{x}$ and $c_{x}$. Likewise, $f_{y}$ and $c_{y}$ can be obtained by solving the second system of linear equations.

## 2 Solutions (to-be-added)
Methods to solve for the intrinsic parameters can be categorized into either direct computation, or numerical optimization.

To use the solvers, your LUT must be a numpy array $lut$ with shape $(h,w,3)$, where indexing $lut[i,j]$ provides the corresponding ray $[X,Y,Z]$. An example using a least-squares solver is shown below.
```
from utils import pixAndRay
from solver import leastSquares

coords_2d, rays_3d = pixAndRay(lut)
K_approx = leastSquares(coords_2d, rays_3d)
```

A `demo_lstsq.py` script is provided that solves 4 different LUTs using direct least-squares computation.
#### 2.1 Least-Squares solution (direct computation)
Given an overdetermined system of linear equations $Ax = b$, we can obtain the least-squares solution $\hat{x} = (A^TA)^{-1}A^Tb$ through direct computation.
