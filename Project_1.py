import numpy as np
import time

# -> NUMPY FUNDAMENTALS

print("\n ARRAY CREATION, INDEXING & SLICING:")

# Create arrays
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Indexing
print("Index 2:", arr[2])

# Slicing
print("Slice 1:4:", arr[1:4])

# 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("2D Array:\n", matrix)

# -> MATHEMATICAL & STATISTICAL OPERATIONS

print("\n MATHEMATICAL & STATISTICAL OPERATIONS:")
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Std Deviation:", arr.std())
print("Min:", arr.min())
print("Max:", arr.max())

# Axis-wise operations
print("Row-wise sum:", matrix.sum(axis=1))
print("Column-wise sum:", matrix.sum(axis=0))

# -> RESHAPING & BROADCASTING

print("\n RESHAPING & BROADCASTING:")

# Reshape
reshaped = arr.reshape(5, 1)
print("Reshaped to (5,1):\n", reshaped)

# Broadcasting example
broadcast_result = arr + 5
print("Broadcast arr + 5:", broadcast_result)

matrix_add = matrix + arr[:3]   # broadcast row-wise
print("Broadcasting 1D -> 2D:\n", matrix_add)

# -> SAVE & LOAD NUMPY ARRAYS

print("\n SAVE & LOAD NUMPY ARRAYS:")

np.save("my_array.npy", arr)
loaded = np.load("my_array.npy")

print("Saved & Loaded Array:", loaded)

# -> NUMPY VS PYTHON LIST PERFORMANCE

print("\n NUMPY VS PYTHON LIST PERFORMANCE:")

# Python list performance
py_list = list(range(1_000_000))
start = time.time()
py_list_result = [x * 2 for x in py_list]
python_time = time.time() - start

# NumPy performance
np_arr = np.arange(1_000_000)
start = time.time()
np_arr_result = np_arr * 2
numpy_time = time.time() - start

print(f"Python list time: {python_time:.6f} seconds")
print(f"NumPy array time: {numpy_time:.6f} seconds")

print("\n NumPy is faster by:",
      round(python_time / numpy_time, 2), "times!")
