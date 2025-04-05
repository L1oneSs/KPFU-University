import numpy as np

def quadratic_bezier(p0, p1, p2, num_points=1000):
    t = np.linspace(0, 1, num_points)
    x = ((1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]).astype(int)
    y = ((1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]).astype(int)

    return x, y

def linear_bezier(p0, p1, num_points=1000):
    t = np.linspace(0, 1, num_points)
    x = ((1 - t) * p0[0] + t * p1[0]).astype(int)
    y = ((1 - t) * p0[1] + t * p1[1]).astype(int)

    return x, y

def cubic_bezier(p0, p1, p2, p3, num_points=1000):
    t = np.linspace(0, 1, num_points)
    x = ((1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] +
         3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]).astype(int)
    y = ((1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] +
         3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]).astype(int)

    return x, y
