import numpy as np
import torch
import torch.nn as nn
import pandas as pd
import matplotlib.pyplot as plt
import os

import linearRegression
import  multiLayerPerceptron

device = 'cuda' if torch.cuda.is_available() else 'cpu'

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
torch.manual_seed(1)
if device == 'cuda':
    torch.cuda.manual_seed_all(1)
readMergePath = r"..\\Kiwoom\\종목별주가추출"
flist = os.listdir(readMergePath)
xlsx_list = [x.split('.')[0] for x in flist if x.endswith('.xlsx')]

#codeName = df.iloc[1:2, 1:]

"""
y = []      #실제 데이터 값 : 주가
for i in codeName:
    y.append(torch.FloatTensor(df[i].to_list()))
"""

for stockName in xlsx_list:
    df = pd.DataFrame(pd.read_excel(f"{readMergePath}\\{stockName}.xlsx"))
    #학습용 독립변수 : x값
    x = torch.FloatTensor(df['일자'].apply(lambda n: int(str(n)[:6])).to_list()).to(device)
    x_date = np.array(df['일자'].apply(lambda n: str(n)[:4] + '-' + str(n)[4:6]).to_list())
    y = torch.FloatTensor(df[stockName]).to(device)

    #ret = linearRegression.calcRegression(x, y, stockName);
    #ret = ret.detach().numpy()
    #print(f"linearFunc : {linearFunc}")

    model = multiLayerPerceptron.calcPerceptron(device, x, y)
    ret = np.array(model.detach().cpu())
    #print(ret, type(ret))


    print(f"{stockName} 비교 그래프 출력중...")

    curPlot = plt.figure(figsize=(20, 10))
    plt.xticks(rotation=45)
    plt.title(f"{stockName} 예측 모델 비교")
    plt.xlabel("시점")
    plt.ylabel("주가")

    y = np.array(y.detach().cpu())
    plt.plot(x_date, y, 'b', label=f"{stockName} 실제 주가")
    plt.plot(x_date, ret, 'r', linestyle='dotted', label=f"{stockName} 선형 모델")
    plt.legend(loc='upper left')

    # x, y축 조정
    ax = curPlot.gca()
    ax.xaxis.set_major_locator(plt.MaxNLocator(30))
    ax.yaxis.set_major_locator(plt.MaxNLocator(10))

plt.show()
