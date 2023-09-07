import utils as util
import numpy as np
import os

error = np.random.rand(30,30)
print(error)
num_anom = np.count_nonzero(error >=  0.99)


print(num_anom)

error2 = np.array([[1, 2, 3], [4, 5, 6]])
num_anom2 = np.count_nonzero(error2 > 2)
print(num_anom2)
