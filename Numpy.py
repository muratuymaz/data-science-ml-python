import numpy as np

my_list = [10,20,30,40]

# print(type(my_list))


my_numpy_array = np.array(my_list)

# print(my_numpy_array)

array = np.random.random(5)

array2 = np.zeros(10)

my_list1 = [1,2]

my_list2 = [2,3]

# bu toplam sonucunda [1,2,2,3] dizisi olusur!
my_list1 + my_list2

my_numpy_list1 = np.array(my_list1)

my_numpy_list2 = np.array(my_list2)

# bu toplam sonucunda ise ayni indekslerde tutulan degerler toplaniyor!
# iki dizinin uzunlugu ayni olmali bu yuzden
sum = my_numpy_list1 + my_numpy_list2

# arange ile diziyi olusturabiliyoruz
np_array = np.arange(1,10,2)

# random ile rastgele bir dizi olusturabiliyoruz
np_array = np.random.randint(1,50,5)

# matrixler
my_matrix = np.random.randint(1,10,size=(2,5))
my_matrix = np.ones((2,3,5))
my_matrix = np.array([[5,10],[15,20]])
my_matrix = my_matrix.sum()

# print(my_matrix)

# matrix aritmetigi
first_matrix = np.array([[10,20],[30,40]])
second_matrix = np.array([[5,15],[25,35]])

my_matrix = first_matrix + second_matrix

# print(my_matrix)

# matrix dot product
first_matrix = np.array([[10,20,30]])
second_matrix = np.array([[2,3],[3,2],[5,1]])
print("1. matrix boyutu:",first_matrix.shape) #(a,b) - bunun row yani satir sayisi ile 
print("2. matrix boyutu:",second_matrix.shape) # (b,c) - bunun column yani kolon sayisi ayni olmali
print("1.matrix:")
for i in first_matrix:
    print(i)
print("2.matrix:")
for i in second_matrix:
    print(i)
print("1. ve 2. matrixlerin carpimi:")
for i in first_matrix.dot(second_matrix):
    print(i)