from pykiwoom.kiwoom import *
import datetime
import time

import priceCutting as cutter
import priceTable as tabler

out_path = r".\종목별정보"

# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect()

# 전종목 종목코드
#kospi = kiwoom.GetCodeListByMarket('0')
#kosdaq = kiwoom.GetCodeListByMarket('10')
#code = kospi + kosdaq

#삼전, 하이닉스
code = ["005930", "000660"]

# 문자열로 오늘 날짜 얻기
now = datetime.datetime.now()
today = now.strftime("%Y%m%d")

print(f"{kiwoom.GetMasterCodeName(code[0])} {kiwoom.GetMasterCodeName(code[1])} {code}\n")

#차트 불러오기 후 엑셀 파일 생성
for x in code:
    df = kiwoom.block_request("opt10083",
                              종목코드=x,
                              기준일자=today,
                              수정주가구분=1,
                              output="주식월봉차트조회",
                              next=0)
    """
    df2 = kiwoom.block_request("opt10083",
                              종목코드=x,
                              기준일자= df['일자'].iloc[-1],
                              수정주가구분=1,
                              output="주식월봉차트조회",
                              next=0)
    df2.index = [num + len(df) - 1 for num in range(len(df2))]
    """

    out_name = f"{out_path}/{kiwoom.GetMasterCodeName(x)}.xlsx"

    #mergeDf = pd.concat([df, df2.iloc[1:]])
    df.to_excel(out_name)
    time.sleep(3.6)

cutter.priceCut()
tabler.makeTable()