import time
import datetime
import json
import requests


#Preços em dólares
def bitfinex_btc(): 
    bitFinexTick1 = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    return bitFinexTick1.json()['last_price']

def bitfinex_eth(): 
    bitFinexTick2 = requests.get("https://api.bitfinex.com/v1/ticker/ethusd")
    return bitFinexTick2.json()['last_price']


def bitfinex_ltc(): 
    bitFinexTick3 = requests.get("https://api.bitfinex.com/v1/ticker/ltcusd")
    return bitFinexTick3.json()['last_price']

def bitfinex_xrp(): 
    bitFinexTick4 = requests.get("https://api.bitfinex.com/v1/ticker/xrpusd")
    return bitFinexTick4.json()['last_price']

#def bitfinex_bch(): 
#    bitFinexTick5 = requests.get("https://api.bitfinex.com/v1/ticker/bchusd")
#    return bitFinexTick5.json()['last_price']

def bitfinex_xmr(): 
    bitFinexTick6 = requests.get("https://api.bitfinex.com/v1/ticker/xmrusd")
    return bitFinexTick6.json()['last_price']

def bitfinex_sng(): 
    bitFinexTick7 = requests.get("https://api.bitfinex.com/v1/ticker/sngusd")
    return bitFinexTick7.json()['last_price']

def bitfinex_trx(): 
    bitFinexTick8 = requests.get("https://api.bitfinex.com/v1/ticker/trxusd")
    return bitFinexTick8.json()['last_price']

def bitfinex_zec(): 
    bitFinexTick9 = requests.get("https://api.bitfinex.com/v1/ticker/zecusd")
    return bitFinexTick9.json()['last_price']

def bitfinex_eos(): 
    bitFinexTick10 = requests.get("https://api.bitfinex.com/v1/ticker/eosusd")
    return bitFinexTick10.json()['last_price']

def bitfinex_omg(): 
    bitFinexTick11 = requests.get("https://api.bitfinex.com/v1/ticker/omgusd")
    return bitFinexTick11.json()['last_price']

def bitfinex_etc(): 
    bitFinexTick12 = requests.get("https://api.bitfinex.com/v1/ticker/etcusd")
    return bitFinexTick12.json()['last_price']

def bitfinex_gnt(): 
    bitFinexTick13 = requests.get("https://api.bitfinex.com/v1/ticker/gntusd")
    return bitFinexTick13.json()['last_price']

def bitfinex_btg(): 
    bitFinexTick14 = requests.get("https://api.bitfinex.com/v1/ticker/btgusd")
    return bitFinexTick14.json()['last_price']

#Preços em Bitcoins

def bitfinex_beth(): 
    bitFinexTick2b = requests.get("https://api.bitfinex.com/v1/ticker/ethbtc")
    return bitFinexTick2b.json()['last_price']
def bitfinex_bltc(): 
    bitFinexTick3 = requests.get("https://api.bitfinex.com/v1/ticker/ltcbtc")
    return bitFinexTick3.json()['last_price']

def bitfinex_bxrp(): 
    bitFinexTick4 = requests.get("https://api.bitfinex.com/v1/ticker/xrpbtc")
    return bitFinexTick4.json()['last_price']

#def bitfinex_bch(): 
#    bitFinexTick5 = requests.get("https://api.bitfinex.com/v1/ticker/bchbtc")
#    return bitFinexTick5.json()['last_price']

def bitfinex_bxmr(): 
    bitFinexTick6 = requests.get("https://api.bitfinex.com/v1/ticker/xmrbtc")
    return bitFinexTick6.json()['last_price']

def bitfinex_bsng(): 
    bitFinexTick7 = requests.get("https://api.bitfinex.com/v1/ticker/sngbtc")
    return bitFinexTick7.json()['last_price']

def bitfinex_btrx(): 
    bitFinexTick8 = requests.get("https://api.bitfinex.com/v1/ticker/trxbtc")
    return bitFinexTick8.json()['last_price']

def bitfinex_bzec(): 
    bitFinexTick9 = requests.get("https://api.bitfinex.com/v1/ticker/zecbtc")
    return bitFinexTick9.json()['last_price']

def bitfinex_beos(): 
    bitFinexTick10 = requests.get("https://api.bitfinex.com/v1/ticker/eosbtc")
    return bitFinexTick10.json()['last_price']

def bitfinex_bomg(): 
    bitFinexTick11 = requests.get("https://api.bitfinex.com/v1/ticker/omgbtc")
    return bitFinexTick11.json()['last_price']

def bitfinex_betc(): 
    bitFinexTick12 = requests.get("https://api.bitfinex.com/v1/ticker/etcbtc")
    return bitFinexTick12.json()['last_price']

def bitfinex_bgnt(): 
    bitFinexTick13 = requests.get("https://api.bitfinex.com/v1/ticker/gntbtc")
    return bitFinexTick13.json()['last_price']

def bitfinex_bbtg(): 
    bitFinexTick14 = requests.get("https://api.bitfinex.com/v1/ticker/btgbtc")
    return bitFinexTick14.json()['last_price']



#Preços em Ethereum

def bitfinex_ebtc(): 
    bitFinexTick1e = requests.get("https://api.bitfinex.com/v1/ticker/btceth")
    return bitFinexTick1e.json()['last_price']

def bitfinex_eltc(): 
    bitFinexTick3 = requests.get("https://api.bitfinex.com/v1/ticker/ltceth")
    return bitFinexTick3.json()['last_price']

def bitfinex_exrp(): 
    bitFinexTick4 = requests.get("https://api.bitfinex.com/v1/ticker/xrpeth")
    return bitFinexTick4.json()['last_price']

#def bitfinex_ebch(): 
#    bitFinexTick5 = requests.get("https://api.bitfinex.com/v1/ticker/bcheth")
#    return bitFinexTick5.json()['last_price']

def bitfinex_exmr(): 
    bitFinexTick6 = requests.get("https://api.bitfinex.com/v1/ticker/xmreth")
    return bitFinexTick6.json()['last_price']

def bitfinex_esng(): 
    bitFinexTick7 = requests.get("https://api.bitfinex.com/v1/ticker/sngeth")
    return bitFinexTick7.json()['last_price']

def bitfinex_etrx(): 
    bitFinexTick8 = requests.get("https://api.bitfinex.com/v1/ticker/trxeth")
    return bitFinexTick8.json()['last_price']

def bitfinex_ezec(): 
    bitFinexTick9 = requests.get("https://api.bitfinex.com/v1/ticker/zeceth")
    return bitFinexTick9.json()['last_price']

def bitfinex_eeos(): 
    bitFinexTick10 = requests.get("https://api.bitfinex.com/v1/ticker/eoseth")
    return bitFinexTick10.json()['last_price']

def bitfinex_eomg(): 
    bitFinexTick11 = requests.get("https://api.bitfinex.com/v1/ticker/omgeth")
    return bitFinexTick11.json()['last_price']

def bitfinex_eetc(): 
    bitFinexTick12 = requests.get("https://api.bitfinex.com/v1/ticker/etceth")
    return bitFinexTick12.json()['last_price']

def bitfinex_egnt(): 
    bitFinexTick13 = requests.get("https://api.bitfinex.com/v1/ticker/gnteth")
    return bitFinexTick13.json()['last_price']

def bitfinex_ebtg(): 
    bitFinexTick14 = requests.get("https://api.bitfinex.com/v1/ticker/btgeth")
    return bitFinexTick14.json()['last_price']



while True:

    print ('###################--BITFINEX em DÓLAR--########################')
    print ('Hora: ', datetime.datetime.now())

    bitfinexlivebtc = float(bitfinex_btc())
    bitfinexliveeth = float(bitfinex_eth())
    bitfinexliveltc = float(bitfinex_ltc())
    bitfinexlivexrp = float(bitfinex_xrp())
    #bitfinexlivebch = float(bitfinex_bch())
    bitfinexlivexmr = float(bitfinex_xmr())
    bitfinexlivebtg = float(bitfinex_btg())
    bitfinexlivesng = float(bitfinex_sng())
    bitfinexlivetrx = float(bitfinex_trx())
    bitfinexlivezec = float(bitfinex_zec())
    bitfinexliveeos = float(bitfinex_eos())
    bitfinexliveomg = float(bitfinex_omg())
    bitfinexliveetc = float(bitfinex_etc())
    bitfinexlivegnt = float(bitfinex_gnt())

    

    print ('BTC = U$',bitfinexlivebtc)
    print ('ETH = U$',bitfinexliveeth)
    print ('LTC = U$',bitfinexliveltc)
    print ('XRP = U$',bitfinexlivexrp)
    #print ('BCH = U$',bitfinexlivebch)
    print ('XMR = U$',bitfinexlivexmr)
    print ('BTG = U$',bitfinexlivebtg)
    print ('SNG = U$',bitfinexlivesng)
    print ('TRX = U$',bitfinexlivetrx)
    print ('ZEC = U$',bitfinexlivezec)
    print ('EOS = U$',bitfinexliveeos)
    print ('OMG = U$',bitfinexliveomg)
    print ('ETC = U$',bitfinexliveetc)
    print ('GNT = U$',bitfinexlivegnt)
    

    print ('###################--BITFINEX em BTC--########################')
    
    bitfinexliveeth = float(bitfinex_beth())
    bitfinexliveltc = float(bitfinex_bltc())
    bitfinexlivexrp = float(bitfinex_bxrp())
    #bitfinexlivebch = float(bitfinex_bbch())
    bitfinexlivexmr = float(bitfinex_bxmr())
    bitfinexlivebtg = float(bitfinex_bbtg())
    bitfinexlivesng = float(bitfinex_bsng())
    bitfinexlivetrx = float(bitfinex_btrx())
    bitfinexlivezec = float(bitfinex_bzec())
    bitfinexliveeos = float(bitfinex_beos())
    bitfinexliveomg = float(bitfinex_bomg())
    bitfinexliveetc = float(bitfinex_betc())
    bitfinexlivegnt = float(bitfinex_bgnt())
    
    print ('ETH = BTC',bitfinexliveeth)
    print ('LTC = BTC',bitfinexliveltc)
    print ('XRP = BTC',bitfinexlivexrp)
    #print ('BCH = BTC',bitfinexlivebch)
    print ('XMR = UBTC',bitfinexlivexmr)
    print ('BTG = BTC',bitfinexlivebtg)
    print ('SNG = BTC',bitfinexlivesng)
    print ('TRX = BTC',bitfinexlivetrx)
    print ('ZEC = BTC',bitfinexlivezec)
    print ('EOS = BTC',bitfinexliveeos)
    print ('OMG = BTC',bitfinexliveomg)
    print ('ETC = BTC',bitfinexliveetc)
    print ('GNT = BTC',bitfinexlivegnt)

    print ('###################--BITFINEX em ETH--########################')

    #bitfinexlivebtc = float(bitfinex_ebtc())

    #bitfinexliveltc = float(bitfinex_eltc())
    #bitfinexlivexrp = float(bitfinex_exrp())
    #bitfinexlivebch = float(bitfinex_ebch())
    #bitfinexlivexmr = float(bitfinex_exmr())
    #bitfinexlivebtg = float(bitfinex_ebtg())
    bitfinexlivesng = float(bitfinex_esng())
    bitfinexlivetrx = float(bitfinex_etrx())
    #bitfinexlivezec = float(bitfinex_ezec())
    bitfinexliveeos = float(bitfinex_eeos())
    bitfinexliveomg = float(bitfinex_eomg())
    #bitfinexliveetc = float(bitfinex_eetc())
    bitfinexlivegnt = float(bitfinex_egnt())

    

    #print ('BTC = ETH',bitfinexlivebtc)
    #print ('ETH = ETH',bitfinexliveeth)
    #print ('LTC = ETH',bitfinexliveltc)
    #print ('XRP = ETH',bitfinexlivexrp)
    #print ('BCH = ETH',bitfinexlivebch)
    #print ('XMR = ETH',bitfinexlivexmr)
    #print ('BTG = ETH',bitfinexlivebtg)
    print ('SNG = ETH',bitfinexlivesng)
    print ('TRX = ETH',bitfinexlivetrx)
    #print ('ZEC = ETH',bitfinexlivezec)
    print ('EOS = ETH',bitfinexliveeos)
    print ('OMG = ETH',bitfinexliveomg)
    #print ('ETC = ETH',bitfinexliveetc)
    print ('GNT = ETH',bitfinexlivegnt)
    
    time.sleep(120)
    

    
