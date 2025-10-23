# Getting familiar with 1D, 2D and 3D arrays
import numpy as np

array1D = np.array([2, 5, 9, 7])
array2D = np.array([[0.2, 5.1, 9], [26.9, 2.5, 0.7]])
array3D = np.array([[[0.2, 5.1, 9], [26.9, 2.5, 0.7]], [[1, 1, 1], [1, 1, 1]]])

# Now print the shape of the differen arrays
print(f"The shape of the array1D is {array1D.shape}")
print(f"The shape of the array2D is {array2D.shape}")
print(f"The shape of the array3D is {array3D.shape}\n")

# Print the maximum value
print(f"The maximum value in the first column of array2D is {np.max(array2D[:, 0])}")

# Print the numbers marked in red
print(f"The number marked red in the 1D array  is {array1D[0]}")
print(f"The number marked red in the 2D array  is {array2D[0, 1]}")
print(f"The number marked red in the 3D array  is {array3D[0, 1, 2]}")
