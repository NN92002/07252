import numpy as np #引路numpy套件取名為np

# 創建 NumPy 數組
arr = np.array([1, 2, 3, 4, 5]) #建構一維陣列
print("1D array:", arr)

# 2D 數組
arr_2d = np.array([[1, 2, 3], [4, 5, 6]]) #建構2列3行二微陣列
print("2D array:\n", arr_2d)

# 基本操作
print("Array shape:", arr_2d.shape) # shape：回傳陣列的形狀 (列數, 行數)，這裡是 (2, 3)
print("Array dimension:", arr_2d.ndim) # ndim：回傳陣列的維度數，這裡是 2（表示是 2D 陣列）
print("Array size:", arr_2d.size)  # size：回傳陣列中所有元素的總數，這裡是 6（2*3）

# 數學運算
print("Mean:", np.mean(arr_2d))  # mean：計算所有元素的平均值，這裡是 3.5
print("Sum:", np.sum(arr_2d)) # sum：計算所有元素的總和，這裡是 21


print("Add 1 to all elements:\n", arr_2d + 1)
# arr_2d + 1：將每個元素加 1，結果是 [[2, 3, 4], [5, 6, 7]]