import numpy

numbers = numpy.array([5.0,"10",15,20])
print(numbers)
print(numbers.dtype ) # 显示类型
matric=numpy.ones((3,4))
vector=numpy.array([0,2,10,5,4])
equal_five_ten = (vector == 10) | (vector == 5)#判断矩阵元素是否等于5或者10
vector = vector.astype(float)  # 矩阵里面的元素装换类型
print(matric.sum(axis=0))  # 0是按列求和，1是按照行求和
print(vector.ndim)  # 矩阵的维度
