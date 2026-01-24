import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ageList = [22, 25, 43, 46, 52, 55, 57, 60, 62, 70, 75, 80]
weightList = [60, 65, 70, 72, 68, 75, 78, 80, 85, 90, 95, 100]

df = pd.DataFrame({
    'Age': ageList,
    'Weight': weightList
})
# plt.plot(df['Age'], df['Weight'], marker='o', linestyle='-', color='b')
# print(df)
# plt.show()

# numpy
npAge = np.array(ageList)
npWeight = np.array(weightList)

numpy_arr1 = np.linspace(0, 10, 20)
numpy_arr2 = numpy_arr1 ** 3

# plt.subplot(1,2,1)
# plt.plot(numpy_arr1, numpy_arr2, 'r')
# plt.subplot(1,2,2)
# plt.plot(ageList, weightList, 'g*-')
# my_figure = plt.figure()
# figure_axes = my_figure.add_axes([0.1, 0.1, 0.8, 0.8])
# figure_axes.plot(numpy_arr1, numpy_arr2, 'b')
# figure_axes.set_xlabel('X Label')
# figure_axes.set_ylabel('Y Label')
# figure_axes.set_title('Title')

new_figure = plt.figure(dpi=100)
new_axes = new_figure.add_axes([0.1, 0.1, 0.8, 0.8])
new_axes.plot(numpy_arr1, numpy_arr1**2, 'y',label='Weight^2')
new_axes.plot(numpy_arr1, numpy_arr1**3, 'b',label='Weight^3')
plt.legend()
plt.show()