import math
import numpy as np

rpms = 840 # Rotations per minute
rows = 2250 # Pixels

center = np.array([2069, 1245])

a1 = np.array([[1504, 576],  [1304, 844], [1802, 408]])
a2 = np.array([[1386, 702], [1240, 1000], [1647, 482]])
a2p = np.array([[1214, 1171],  [1495, 1908], [1565, 541]])

radius = np.median(np.linalg.norm(np.concatenate((a1, a2, a2p)) - center, axis=1))

# Rotations per second (radians)
rps_rad = (rpms / 60) * math.pi * 2

y = (2*rows * (np.arccos(np.linalg.norm(a1 - a2, axis=1) / (2*radius))  - np.arccos(np.linalg.norm(a1 - a2p, axis=1) / (2*radius))))
x = (rps_rad * np.abs(a2p.T[1] - a1.T[1])) 
t =  y / x

# Linear least squares fit
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
A = np.vstack([x, np.ones(len(x))]).T
t, c = np.linalg.lstsq(A, y, rcond=None)[0]

print("Readout time: %s ms" % round(t * 1000, 2))

import matplotlib.pyplot as plt
_ = plt.plot(x, y, 'o', label='Points', markersize=10)
_ = plt.plot(x, t*x + c, 'r', label='Readout time')
_ = plt.legend()
plt.show()