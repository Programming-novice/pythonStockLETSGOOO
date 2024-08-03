import numpy as np
import torch
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import linearRegression

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
torch.manual_seed(1)

readMergePath = r"..\\Kiwoom\\종목별주가추출\\merge.xlsx"
df = pd.DataFrame(pd.read_excel(readMergePath))

codeName = df.iloc[1:2, 1:]
x = torch.FloatTensor(df['일자'].apply(lambda n: int(str(n)[:6])).to_list()) #학습용 독립변수 : x값
x_date = np.array(df['일자'].apply(lambda n: str(n)[:4] + '-' + str(n)[4:6]).to_list())
#x_date = x_date.astype(str)

#y = torch.FloatTensor(df['삼성전자'].to_list())

y = []      #실제 데이터 값 : 주가
for i in codeName:
    y.append(torch.FloatTensor(df[i].to_list()))

for arg_y, name in zip(y, codeName):
    linearFunc = linearRegression.calcRegression(x, arg_y, name);
    linearFunc = linearFunc.detach().numpy()
    #print(f"linearFunc : {linearFunc}")

    print(f"{name} 비교 그래프 출력중...")

    curPlot = plt.figure(figsize=(20, 10))
    #plt.xlim(x_date[0], x_date[-1])
    plt.xticks(rotation=45)
    plt.title(f"{name} 선형 회귀 모델 비교")
    plt.xlabel("시점")
    plt.ylabel("주가")

    plt.plot(x_date, arg_y, 'b', label=f"{name} 실제 주가")
    plt.plot(x_date, linearFunc, 'r', label=f"{name} 선형 모델")
    plt.legend(loc='upper left')


    # 주가 점선 추가
    ax = curPlot.gca()
    #for x in ax.get_yticks():
    #    if x > 0 and x < 250000:
    #        plt.axhline(y=int(x), xmin=0, xmax=1, color='green', linestyle='dotted')

    # x, y축 조정
    #ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_locator(plt.MaxNLocator(30))
    ax.yaxis.set_major_locator(plt.MaxNLocator(10))
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))


plt.show()
