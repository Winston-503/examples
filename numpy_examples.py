import numpy as np

# Creating an array
np.array([1, 2, 3])
np.array([1, 2, 3], dtype='float32')
np.arange(0, 10, 2)
np.zeros(10)
np.ones((3, 5))
np.full((2, 2), 54)
np.linspace(0, 1, 5)
np.random.random((3, 3)) # random from 0 to 1
np.random.normal(0, 1, (3, 3)) # 0 - mediana, 1 - scale
np.eye(3)
np.arange(9).reshape((3,3))

arr = np.array([1, 2, 3])
arr[:, np.newaxis] # to colomn vector - вектор-столбец
# arr.reshape(arr.size, 1)
arr[np.newaxis, :] # to row vector - вектор-строка
# arr.reshape(1, arr.size)

first = np.arange(1, 5)
second = 1 / first

# Инструменты доступа NumPy

# индексация (arr[2, 1]) 
# срезы (arr[:,1:5]) 
# маскирование (arr[arr > 0])  
# «прихотливуя» индексация (arr[0,[1,5]]) 
# их комбинации (arr[:,[1,5]])
