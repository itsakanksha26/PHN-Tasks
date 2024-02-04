import numpy as np


arr1 = np.array([[1, 2, 3], [4, 5, 0]])

print("Shape of the original array:", arr1.shape)

arr2 = np.array([6, 7, 8, 9, 10, 11])

arr2_reshaped = arr2.reshape(2, 3)

arr_concatenated = np.concatenate((arr1, arr2_reshaped), axis=1)

print("Concatenated array:\n", arr_concatenated)

print("Mean:", np.mean(arr_concatenated))
print("Median:", np.median(arr_concatenated))
print("Standard deviation:", np.std(arr_concatenated))
