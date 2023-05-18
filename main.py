import requests
import sched, time, os
import csv
from datetime import datetime
# import pandas as pd

s = sched.scheduler(time.time, time.sleep)
url = 'https://www.okx.com'
# tickers = pd.DataFrame((requests.get(url+'/api/v5/market/tickers?instType=SPOT').json())['data'])
# tickers = tickers.drop('instType', axis=1)
# tickers.tail().T


def top_line(ticker_info):
    instrument_name = ticker_info['data'][0]['instId']
    mid_px = (float(ticker_info['data'][0]['bidPx']) + float(ticker_info['data'][0]['bidPx'])) / 2
    instrument = (instrument_name, mid_px)
    print(instrument)
    return instrument


def ticker_store_ETH():
    ETH_USD, ETH_USDT, ETH_USDC = (), (), ()
    ETH_USD = top_line(requests.get(url+'/api/v5/market/ticker?instId=ETH-USD-SWAP').json())
    ETH_USDT = top_line(requests.get(url+'/api/v5/market/ticker?instId=ETH-USDT-SWAP').json())
    ETH_USDC = top_line(requests.get(url+'/api/v5/market/ticker?instId=ETH-USDC-SWAP').json())
    NEWLINE = str(ETH_USD[1]) + "," + str(ETH_USDT[1]) + "," + str(ETH_USDC[1])
    return NEWLINE


def ticker_store_BTC():
    BTC_USD, BTC_USDT, BTC_USDC = (), (), ()
    BTC_USD = top_line(requests.get(url+'/api/v5/market/ticker?instId=BTC-USD-SWAP').json())
    BTC_USDT = top_line(requests.get(url+'/api/v5/market/ticker?instId=BTC-USDT-SWAP').json())
    BTC_USDC = top_line(requests.get(url+'/api/v5/market/ticker?instId=BTC-USDC-SWAP').json())
    NEWLINE = str(BTC_USD[1]) + "," + str(BTC_USDT[1]) + "," + str(BTC_USDC[1])
    return NEWLINE


def ticker_store_LTC():
    LTC_USD, LTC_USDT, LTC_USDC = (), (), ()
    LTC_USD = top_line(requests.get(url+'/api/v5/market/ticker?instId=LTC-USD-SWAP').json())
    LTC_USDT = top_line(requests.get(url+'/api/v5/market/ticker?instId=LTC-USDT-SWAP').json())
    NEWLINE = str(LTC_USD[1]) + "," + str(LTC_USDT[1])
    return NEWLINE


def do_this(sc):
    main()
    s.enter(9, 1, do_this, (sc,))


def csv_read(add_line):
    from csv import writer
    newline = [add_line]
    with open('Crypto_Price_Snap.txt', mode="at") as csv_file:
        writer = writer(csv_file)
        writer.writerow(newline)
        csv_file.close()


''' # put this in when ready to add timer:  
s.enter(20, 1, do_this, (s,))
s.run()
'''


def main():
    now = datetime.now()
    date_time = now.strftime("%Y%m%d %H:%M:%S")
    ETH = ticker_store_ETH()
    BTC = ticker_store_BTC()
    LTC = ticker_store_LTC()

    add_row = (date_time + "," + ETH + "," + BTC + "," + LTC)
    csv_read(add_row)


s.enter(30, 30, do_this, (s,))
s.run()
main()