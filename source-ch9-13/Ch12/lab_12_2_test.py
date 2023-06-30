#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 12-2 판다스로 울릉도의 바람 세기 분석하기, 322쪽
#
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('d:/data/weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
# 다음과 같은 groupby() 기능을 사용해서 더 간단한 코드 작성가능
means = weather.groupby('month').mean()

#plt.plot(means['평균풍속'], 'red')
means['평균풍속'].plot()
plt.show()