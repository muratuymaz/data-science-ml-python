import numpy as np

newArray = np.random.randint(1,100,20)
# for i in newArray:
#     print(i)
# print(newArray[newArray>=25])

matrixArray = np.array([[10,20],[20,30],[30,40]])

# for i in matrixArray:
#     print(i)
# for i in matrixArray.transpose():
#     print(i)

# math equations - matematik cozumleri yapabiliriz

# 3x + 5y = 24 ve 7x + 4y = 29

A = np.array([[3,5],[7,4]])
B = np.array([24,29])

solution = np.linalg.solve(A,B)

print(solution)