import pandas as pd
import os

def priceCut():
    print("종목별 월봉 주가 추출중...")

    readFilePath = r"./종목별정보"
    outFilePath = r"./종목별주가추출"
    flist = os.listdir(readFilePath)
    close_data = []
    xlsx_list = [ x for x in flist if x.endswith('.xlsx')]

    #종목별 매월 시장가 병합
    for xls in xlsx_list:
        code = xls.split('.')[0]
        df = pd.read_excel(f"{readFilePath}/{xls}")
        df2 = df[['일자', '현재가']].copy()
        df2.rename(columns={'현재가': code}, inplace=True)
        df2 = df2.set_index('일자')
        df2 = df2[::-1]
        close_data.append(df2)

    # concat
    df = pd.concat(close_data, axis=1)
    df.to_excel(f"{outFilePath}\\merge.xlsx")
