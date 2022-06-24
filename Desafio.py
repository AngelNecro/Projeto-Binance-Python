import numpy as np
import pandas as pd
import json
import requests
from datetime import datetime, timedelta


# Pegando data atual
current_data = datetime.now()
# Pegando data 30 dias atras ou seja 1 mês
month_ago_data = current_data - timedelta(30)

# Convertendo data atual em millisegundos
current_millisecond_data = round(datetime.timestamp(current_data) * 1000)
# Convertendo data atual em millisegundos
month_ago_millisecond_data = round(datetime.timestamp(month_ago_data) * 1000)


symbol = 'BTCUSDT'
period = '5m'
lim = ""
startTime = current_millisecond_data
endTime = month_ago_millisecond_data

print("dia inicial : ", startTime)
print("dia final : ", endTime)

# Url da API
url_binance = 'https://fapi.binance.com/futures/data/globalLongShortAccountRatio'


# https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&LIM&startTime=1652604300012&endTime=1653600300000
url = url_binance + '?symbol=' + symbol + '&period=' + period + "&LIM" + \
    lim + "&startTime" + str(startTime) + "&endTime" + str(endTime)

print("url final: ", url)

# Request GET da API transformando em texto
data = json.loads(requests.get(url).text)

print("json: ", data)
