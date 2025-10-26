from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from stocks_code import finished_dict

def vix_sentiment(vix_change: float, vix_price: float) -> int:
    if vix_price > 25 and vix_change > 5:  # High VIX and large increase
        return 1  # Very Bearish
    elif vix_price > 20 and vix_change > 0:  # Moderately high VIX and rising
        return 2  # Bearish
    elif vix_price < 18 and vix_change < 0:  # Low VIX and decreasing
        return 3  # Bullish
    elif vix_price < 15 and vix_change < -5:  # Very low VIX and large drop
        return 4  # Very Bullish
    else:
        return 2  # Default to Bearish if unclear

def get_golor(c:float):
    if c < 0:
        return 'red'
    return 'green'

############################################################################
#open image
main_img = Image.open('stock_sum_temp.png')
time_font = ImageFont.truetype('DMSans-ExtraBold.ttf', 60)
inf_font = ImageFont.truetype('DMSans-ExtraBold.ttf', 20)

############################################################################
#put the time onto the image
time = datetime.now()
time = time.strftime('%d/%m/%y | %H:%M')
d = ImageDraw.Draw(main_img)
d.text((1300, 153), time, fill='white', font=time_font)

############################################################################
#put the stocks and value
STOCK_PRICE_X = 1615
STOCK_PRICE_y = 405
CRYPTO_PRICE_X = STOCK_PRICE_X - 480
INDEXES_PRICE_X = CRYPTO_PRICE_X - 482
BOX1_X = 95
BOX1 = (BOX1_X, STOCK_PRICE_y - 20)
BOX2 = (BOX1_X + 100, STOCK_PRICE_y - 20)
BOX3 = (BOX1_X + 200, STOCK_PRICE_y - 20)

inf = ImageDraw.Draw(main_img)
for sym in finished_dict:
    price = ''
    change=''
    color = 'black'
    position = []
    if sym == 'NVDA':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [STOCK_PRICE_X, STOCK_PRICE_y]


    elif sym == 'TSLA':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [STOCK_PRICE_X, STOCK_PRICE_y + 115]

    elif sym == 'META':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [STOCK_PRICE_X, STOCK_PRICE_y + 115 * 2]

    elif sym == 'MSTR':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [STOCK_PRICE_X, STOCK_PRICE_y + 115 * 3]

    elif sym == 'AAPL':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [STOCK_PRICE_X, STOCK_PRICE_y + 115 * 4]

    elif sym == 'BTCUSD':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [CRYPTO_PRICE_X, STOCK_PRICE_y]

    elif sym == 'ETHUSD':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [CRYPTO_PRICE_X, STOCK_PRICE_y + 115]

    elif sym == 'XRPUSD':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [CRYPTO_PRICE_X, STOCK_PRICE_y + 115 * 2]

    elif sym == 'SOLUSD':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [CRYPTO_PRICE_X, STOCK_PRICE_y + 115 * 3]

    elif sym == 'BNBUSD':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [CRYPTO_PRICE_X, STOCK_PRICE_y + 115 * 4]

    elif sym == 'VIX':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [INDEXES_PRICE_X, STOCK_PRICE_y]

        bull = Image.open("bull.webp")
        bear = Image.open("bear.webp")
        bull = bull.resize((80,80))
        bear = bear.resize((80,80))

        sen = vix_sentiment(float(change[:-1]), float(price[:-1]))
        if sen == 1:
            main_img.paste(bear, BOX1)
            main_img.paste(bear, BOX2)
            main_img.paste(bear, BOX3)
        elif sen == 2:
            main_img.paste(bull, BOX1)
            main_img.paste(bear, BOX2)
            main_img.paste(bear, BOX3)
        elif sen == 3:
            main_img.paste(bull, BOX1)
            main_img.paste(bull, BOX2)
            main_img.paste(bear, BOX3)
        elif sen == 4:
            main_img.paste(bull, BOX1)
            main_img.paste(bull, BOX2)
            main_img.paste(bull, BOX3)

    elif sym == 'SPY':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [INDEXES_PRICE_X, STOCK_PRICE_y + 115]

    elif sym == 'QQQ':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [INDEXES_PRICE_X, STOCK_PRICE_y + 115 * 3]
        print(price)

    elif sym == 'TA125':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [INDEXES_PRICE_X, STOCK_PRICE_y + 115 * 4]

    elif sym == 'TOTAL':
        price = finished_dict[sym][0]
        change = finished_dict[sym][1]
        position = [INDEXES_PRICE_X, STOCK_PRICE_y + 115 * 2]

    color = get_golor(float(change[:-1]))
    if position:
        inf.text((position[0], position[1]), str(price), fill=color, font=inf_font)
        inf.text((position[0] + 170, position[1]), str(change), fill=color, font=inf_font)

path = 'completed_img.png'
main_img.save(path)
