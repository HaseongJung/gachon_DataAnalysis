#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 10-4 넘파이 배열의 형태 알아내고 슬라이싱하여 연산하기, 264쪽
#
import numpy as np 
 
x = np.array([[ 1.83, 1.76, 1.69, 1.86, 1.77, 1.73 ], 
              [ 86.0, 74.0, 59.0, 95.0, 80.0, 68.0 ]]) 
y = x[0:2, 1:3] # 넘파이 방식의 슬라이싱
# 아래의 결과는 1차원 행렬이며, x[0:2][1:2], x[0:2][1]과 동일한 결과
z = x[0:2][1:3] # 슬라이싱

#print('x = ', x)
#print('y = ', y)
#print('z = ', z)
print('x shape :', x.shape)
print('y shape :', y.shape)
print('z shape :', z.shape)
print('z values = :', z)

bmi = x[1] / x[0]**2
print('BMI data')
print(bmi)
