import time
import datetime
import json
import requests

#Teste Novadax

def novadax_btc(): 
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BTC_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_btcu(): 
    novadaxTick2 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BTC_USDT")
    return novadaxTick2.json()['data']['lastPrice']

def novadax_bnb():
    novadaxTick3 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BNB_BRL")
    return novadaxTick3.json()['data']['lastPrice']

def novadax_bnbu():
    novadaxTick4 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BNB_USDT")
    return novadaxTick4.json()['data']['lastPrice']

def novadax_bnbe():
    novadaxTick4 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BNB_ETH")
    return novadaxTick4.json()['data']['lastPrice']

def novadax_eth():
    novadaxTick5 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=ETH_BRL")
    return novadaxTick5.json()['data']['lastPrice']

def novadax_ethu():
    novadaxTick6 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=ETH_USDT")
    return novadaxTick6.json()['data']['lastPrice']

def novadax_bch():
    novadaxTick7 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BCH_BRL")
    return novadaxTick7.json()['data']['lastPrice']

def novadax_bchu():
    novadaxTick8 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BCH_USDT")
    return novadaxTick8.json()['data']['lastPrice']


def novadax_xlm():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=XLM_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_xlmu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=XLM_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_xrp():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=XRP_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_xrpu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=XRP_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_trx():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=TRX_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_trxu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=TRX_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_btt():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BTT_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_bttu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=BTT_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_eos():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=EOS_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_eosu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=EOS_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_ada():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=ADA_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_adau():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=ADA_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_link():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=LINK_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_linku():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=LINK_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_dash():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=DASH_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_dashu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=DASH_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_ltc():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=LTC_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_ltcu():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=LTC_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_iota():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=IOTA_BRL")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_iotau():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/ticker?symbol=IOTA_USDT")
    return novadaxTick1.json()['data']['lastPrice']

def novadax_all():
    novadaxTick1 = requests.get("https://api.novadax.com/v1/market/tickers")
    return novadaxTick1.json()['data']

while True:

    print ('###################--NOVADAX--########################')
    print ('Hora: ', datetime.datetime.now())

    novadaxlivebtc = float(novadax_btc())
    novadaxlivebtcu = float(novadax_btcu())
    print ('BTC/BRL: ',novadaxlivebtc, ' BTC/USDT: ', novadaxlivebtcu, ' Cambio: ', novadaxlivebtc/novadaxlivebtcu)

    novadaxliveeth = float(novadax_eth())
    novadaxliveethu = float(novadax_ethu())
    print ('ETH/BRL: ',novadaxliveeth, ' ETH/USDT: ', novadaxliveethu, ' Cambio: ', novadaxliveeth/novadaxliveethu)

    novadaxlivexrp = float(novadax_xrp())
    novadaxlivexrpu = float(novadax_xrpu())
    print ('XRP/BRL: ',novadaxlivexrp, ' XRP/USDT: ', novadaxlivexrpu, ' Cambio: ', novadaxlivexrp/novadaxlivexrpu)

    novadaxliveltc = float(novadax_ltc())
    novadaxliveltcu = float(novadax_ltcu())
    print ('LTC/BRL: ',novadaxliveltc, ' LTC/USDT: ', novadaxliveltcu, ' Cambio: ', novadaxliveltc/novadaxliveltcu)

    novadaxliveall = novadax_all()
    #print ('ALL :',novadaxliveall)

    novadaxlivebnb = float(novadax_bnb())
    novadaxlivebnbu = float(novadax_bnbu())
    novadaxlivebnbe = float(novadax_bnbe())
    print ('BNB/BRL: ',novadaxlivebnb, ' BNB/USDT: ', novadaxlivebnbu, ' Cambio: ', novadaxlivebnb/novadaxlivebnbu)
    #print('TRIANGULAÇÃO BNB-BRL-ETH: ', novadaxlivebnb - (novadaxlivebnbe * novadaxliveeth))

    novadaxlivexlm = float(novadax_xlm())
    print ('XLM = BRL',novadaxlivexlm)

    novadaxlivebnb = float(novadax_bnb())
    print ('BNB = BRL',novadaxlivebnb)

    novadaxliveeos = float(novadax_eos())
    print ('EOS = BRL',novadaxliveeos)

    novadaxlivedash = float(novadax_dash())
    print ('DASH = BRL',novadaxlivedash)



    novadaxliveiota = float(novadax_iota())
    print ('IOTA = BRL',novadaxliveiota)



    time.sleep(1200)
