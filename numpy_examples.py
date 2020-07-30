import numpy as np

# Creating an array
np.array([1, 2, 3])
np.array([1, 2, 3], dtype='float32')
np.arange(0, 10, 2)
np.zeros(10)
np.ones((3, 5))
np.full((2, 2), 54)
np.linspace(0, 1, 5)
np.random.normal(0, 1, (3, 3))  # 0 - mediana, 1 - scale
np.eye(3)
np.arange(9).reshape((3, 3))
np.concatenate([[1, 2, 3], [3, 2, 1]])

arr = np.array([1, 2, 3])
arr[:, np.newaxis]  # to colomn vector
# arr.reshape(arr.size, 1)
arr[np.newaxis, :]  # to row vector
# arr.reshape(1, arr.size)

# Arifmetics +, -, -(unary), *, /, //, **, %
first = np.arange(1, 5)
second = 1 / first
# Aggregation functions - sum, prod, mean, std, min, max, so on

arr1 = np.random.randint(10, size=6)  # one-dimensional
arr2 = np.random.randint(10, size=(3, 4))  # two-dimensional
# Access tools NumPy
# 1. Indexing (arr[2, 1])
# 2. Slicing (arr[:,1:5])
# 3. Masking (arr[arr > 0])
# 4. "Fancy" indexing (arr[0,[1,5]])
# 5. Combinations (arr[:,[1,5]])

# Indexing
arr1[0]
arr1[4]
arr1[-1]
arr1[-2]
arr2[0, 0]
arr2[2, 0]
arr2[2, -1]

# Slicing
arr1[:]
arr1[:5]
arr1[5:]
arr1[2:5]
arr1[::2]
arr1[1::2]
arr1[::-1]
arr2[:2, :3]
arr2[:3, ::2]
arr2[::-1, ::-1]
arr2[0, :]

# Comparison and masking
arr = arr1.copy()
arr < 3
arr >= 10
arr != 0
np.any(arr > 0)
np.all(arr == 1)
arr[arr < 5]

# "Fancy" indexing
ind = [3, 7, 4]
arr[ind]
arr[0, 5, 4] = 0

# Broadcasting
# Broadcasting two arrays together follow these rules:
# 1. If the arrays don't have the same rank then prepend the shape
# of the lower rank array with 1s until both shapes have the same length.
# 2. The two arrays are compatible in a dimension if they have the same size
# in the dimension or if one of the arrays has size 1 in that dimension.
# 3. The arrays can be broadcast together if they are compatible with all dimensions.
# 4. After broadcasting, each array behaves as if it had shape equal to
# the element-wise maximum of shapes of the two input arrays.
# 5. In any dimension where one array had size 1 and the other array had size
# greater than 1, the first array behaves as if it were copied along that dimension.
M = np.ones((2, 3))
a = np.arange(3)
M + a
