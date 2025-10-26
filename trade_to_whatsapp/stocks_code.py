from tradingview_ta import TA_Handler, Interval, Exchange, TradingView
import requests

############################################################
#stocks TA_Handlers#

tesla = TA_Handler(
    symbol='TSLA',
    screener='america',
    exchange='NASDAQ',
    interval=Interval.INTERVAL_1_DAY
)

meta = TA_Handler(
    symbol='META',
    screener='america',
    exchange='NASDAQ',
    interval=Interval.INTERVAL_1_DAY
)

nvda = TA_Handler(
    symbol='NVDA',
    screener='america',
    exchange='NASDAQ',
    interval=Interval.INTERVAL_1_DAY
)

apple = TA_Handler(
    symbol='AAPL',
    screener='america',
    exchange='NASDAQ',
    interval=Interval.INTERVAL_1_DAY
)

mstr = TA_Handler(
    symbol='MSTR',
    screener='america',
    exchange='NASDAQ',
    interval=Interval.INTERVAL_1_DAY
)
##################################################################
#indexes TA_Handlers#
spy = TA_Handler(
    symbol='SPY',
    screener='america',
    exchange='AMEX',
    interval=Interval.INTERVAL_1_DAY
)

vix = TA_Handler(
    symbol='VIX',
    screener='america',
    exchange='TVC',
    interval=Interval.INTERVAL_1_DAY
)

qqq = TA_Handler(
    symbol='QQQ',
    screener='america',
    exchange='NASDAQ',
    interval=Interval.INTERVAL_1_DAY
)

ta125 = TA_Handler(
    symbol='TA125',
    screener='israel',
    exchange='TASE',
    interval=Interval.INTERVAL_1_DAY
)

def get_total_market_cap():
    url = "https://api.coingecko.com/api/v3/global"

    try:
        response = requests.get(url)
        data = response.json()

        total_mc = str(round(data["data"]["total_market_cap"]["usd"]/10**12,2)) + "t"
        total_change_24h = str(round(data["data"]["market_cap_change_percentage_24h_usd"],2)) + "%"

        return total_mc, total_change_24h

    except Exception as e:
        print(f"Error: {e}")
        return None

##################################################################
#crypto TA_Handlers#
btc = TA_Handler(
    symbol='BTCUSD',
    screener='crypto',
    exchange='Binance',
    interval=Interval.INTERVAL_1_DAY
)

eth = TA_Handler(
    symbol='ETHUSD',
    screener='crypto',
    exchange='Binance',
    interval=Interval.INTERVAL_1_DAY
)

xrp = TA_Handler(
    symbol='XRPUSD',
    screener='crypto',
    exchange='Binance',
    interval=Interval.INTERVAL_1_DAY
)

sol = TA_Handler(
    symbol='SOLUSD',
    screener='crypto',
    exchange='Binance',
    interval=Interval.INTERVAL_1_DAY
)

bnb = TA_Handler(
    symbol='BNBUSD',
    screener='crypto',
    exchange='Binance',
    interval=Interval.INTERVAL_1_DAY
)
##################################################################

def get_change_precent(stock:TA_Handler):
    return round(stock.get_analysis().indicators['change'],2)

def get_price(stock:TA_Handler):
    if stock.symbol == 'BTCUSD':
        return round(stock.get_analysis().indicators['close'])
    return round(stock.get_analysis().indicators['close'],2)

def dict_stock_info(arr:list):
    info_dict = {}
    for graph in arr:
        if graph.symbol != 'TA125':
            info_dict[graph.symbol] = (str(get_price(graph)) + "$", str(get_change_precent(graph)) + "%")
        else:
            info_dict[graph.symbol] = (str(get_price(graph)) + " ILS", str(get_change_precent(graph)) + "%")

    return info_dict

total = get_total_market_cap()
indexes_list = [vix, spy, qqq, ta125]
stocks_list = [nvda, tesla, meta, mstr, apple]
crypto_list = [btc, eth, xrp, sol, bnb]

finished_dict = dict_stock_info(stocks_list + crypto_list + indexes_list)
finished_dict['TOTAL'] = total
print(finished_dict)