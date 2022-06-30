import numpy as np
import matplotlib.pyplot as plt
import xlrd3  # 新版本的xlrd不支持打开xlsx格式表格
import pandas as pd
data=pd.read_csv('./simulation_points.csv')
x=data['A'].tolist()
y=data['B'].tolist()
z=data['C'].tolist()


read = xlrd3.open_workbook('./simulation_points.xlsx')
sheet = read.sheet_by_index(0)

k = 1
matrix0 = np.zeros((100, 75))

for i in range(100):
    for j in range(75):
        matrix0[i][j] = sheet.cell_value(k - 1, 0)
        k = k + 1

w = (np.var(matrix0))


# print(matrix)
def circle(matrix):
    matrix1 = np.zeros((100, 75))
    for i in range(100):
        for j in range(75):
            if 0 < i < 99 and 0 < j < 74:
                matrix1[i][j] = (4 * matrix[i][j] + 2 * (
                        matrix[i + 1][j] + matrix[i - 1][j] + matrix[i][j - 1] + matrix[i][j + 1]) + (
                                         matrix[i - 1][j + 1] + matrix[i + 1][j - 1] + matrix[i - 1][j - 1] +
                                         matrix[i + 1][j + 1])) / 16
            elif 99 > i > 0 == j:
                matrix1[i][j] = (8 * matrix[i][j] + 2 * (matrix[i + 1][j] + matrix[i - 1][j] + matrix[i][j + 1]) + (
                        matrix[i + 1][j + 1] + matrix[i - 1][j + 1])) / 16
            elif 0 < i < 99 and j == 74:
                matrix1[i][j] = (8 * matrix[i][j] + 2 * (matrix[i + 1][j] + matrix[i - 1][j] + matrix[i][j - 1]) + (
                        matrix[i + 1][j - 1] + matrix[i - 1][j - 1])) / 16
            elif i == 0 < j < 74:
                matrix1[i][j] = (8 * matrix[i][j] + 2 * (matrix[i][j - 1] + matrix[i][j + 1] + matrix[i + 1][j]) + (
                        matrix[i + 1][j - 1] + matrix[i + 1][j + 1])) / 16
            elif 0 < j < 74 and i == 99:
                matrix1[i][j] = (8 * matrix[i][j] + 2 * (matrix[i - 1][j] + matrix[i][j - 1] + matrix[i][j + 1]) + (
                        matrix[i - 1][j - 1] + matrix[i - 1][j + 1])) / 16
            elif i == 0 and j == 0:
                matrix1[i][j] = (11 * matrix[0][0] + 2 * (matrix[0][1] + matrix[1][0]) + matrix[1][1]) / 16
            elif i == 0 and j == 74:
                matrix1[0][74] = (11 * matrix[0][74] + 2 * (matrix[1][74] + matrix[0][73]) + matrix[1][73]) / 16
            elif i == 99 and j == 0:
                matrix1[99][0] = (11 * matrix[99][0] + 2 * (matrix[98][0] + matrix[99][1]) + matrix[98][1]) / 16
            else:
                matrix[99][74] = (11 * matrix[99][74] + 2 * (matrix[98][74] + matrix[99][73]) + matrix[98][73]) / 16
    return matrix1


old = 0
m = 1 #计数器，记录杨赤忠滤波次数
matrix = circle(matrix0)
n = np.var(matrix)
while (w - n - old) / (w - n) > 0.08:
    old = w - n
    matrix = circle(matrix)
    n = np.var(matrix)
    m = m + 1
else:
    print("杨赤忠滤波迭代次数为{}次".format(m))
    print(matrix)

plt.scatter(x=x, y=y,c=z,cmap='jet')
plt.show()
plt.scatter(x=x, y=y,c=matrix,cmap='jet')
plt.show()
