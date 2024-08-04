import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import os

def makeTable():
    print("종목별 주가 그래프 생성중...")
    plt.rcParams['font.family']='Malgun Gothic'
    plt.rcParams['axes.unicode_minus']=False

    readFilePath = r"./종목별주가추출"
    flist = os.listdir(readFilePath)
    # close_data = []
    xlsx_list = [x for x in flist if x.endswith('.xlsx')]

    for stockName in xlsx_list:
        #File Read
        codeData = pd.DataFrame(pd.read_excel(f"{readFilePath}\\{stockName.split('.')[0]}.xlsx"))
        codeData['일자'] = pd.to_datetime(codeData['일자'].apply(lambda x: str(x)).to_list())

        plt.figure(figsize=(23,10))

        #엑셀파일에서 데이터 추출 후 plot
        plot_X = (codeData['일자']).to_list()
        for c in codeData.iloc[1:2, 1:]:
            plot_Y = codeData[c].to_list()
            plt.plot(plot_X, plot_Y, label=c, marker='o', markersize=2)

        #plot 표시 설정
        plt.xticks(rotation=45)
        plt.legend(loc=2)
        plt.xlim(plot_X[0], plot_X[-1])
        plt.ylim(0, 250000)
        plt.title("과거 월별 주가 그래프")
        plt.xlabel("일자")
        plt.ylabel("주가")

        #주가 점선 추가
        ax = plt.gca()
        for x in ax.get_yticks():
            if x > 0 and x < 250000:
                plt.axhline(y=int(x), xmin=0, xmax=1, color='green', linestyle='dotted')

        #x, y축 조정
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_locator(plt.MaxNLocator(30))
        ax.yaxis.set_major_locator(plt.MaxNLocator(10))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.show()
