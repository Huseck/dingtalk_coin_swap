#coding:utf-8
"""
https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT

https://oapi.dingtalk.com/robot/send?access_token=0db619b4ef27591e18df2b352d6369edf3bb62132eba87975de1fedb8f67f05a
"""
import requests
import json
import time
def getCoinPrice(CoinName):
    price=0
    try:
        r = requests.get("https://api.binance.com/api/v1/ticker/price?symbol={CoinName}USDT".format(CoinName=CoinName))
        print(r.text)
        price = json.loads(r.text)['price'][:-9]
    except:
        pass
    if price==0:
        getCoinPrice(CoinName)
    return int(price)


def dingmessage(coinname,price,message):
# 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=0db619b4ef27591e18df2b352d6369edf3bb62132eba87975de1fedb8f67f05a"
#构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
}
#构建请求数据
    tex = "报警【{}价格:{}】,备注内容:{}".format(coinname,price,message)
    message ={

        "msgtype": "text",
        "text": {
            "content": tex
        },
        "at": {

            # "isAtAll": True
            "isAtAll": False
        }

    }
#对请求的数据进行json封装
    message_json = json.dumps(message)
#发送请求
    info = requests.post(url=webhook,data=message_json,headers=header)
#打印返回的结果
    print(info.text)

if __name__=="__main__":
    #BTC 52500 突破 阻力可以看 54500强阻力位
    BTC_P  = getCoinPrice('BTC')
    # 突破525 站稳可以看 800左右
    COMP_P  = getCoinPrice('COMP')
    #突破241 可以看 340
    LTC_P  = getCoinPrice('LTC')
    BTC_n =0
    COMP_n=0
    LTC_n=0
    while 1:
        if BTC_P > 52000 and BTC_n < 5:
            dingmessage('BTC',BTC_P,"BTC 52000 突破 阻力!")
            BTC_n+=1
        if COMP_P > 525 and COMP_n<5:
            dingmessage('COMP', COMP_P, "COMP 突破525，分析是否可以入场!")
            COMP_n+=1
        if LTC_P > 241 and LTC_n <5:
            dingmessage('LTC',LTC_P,"LTC 突破 241 是否可以入场！")
            LTC_n+=1
        time.sleep(2)
    # dingmessage()
    # getBTCUSDT()
