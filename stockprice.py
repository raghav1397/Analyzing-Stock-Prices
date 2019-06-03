import concurrent.futures
import os

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    key = filename.replace(".csv", "").replace("prices/", "")
    data = data.split("\n")
    data = [d.split(",") for d in data]
    return key, data

results = []
pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
filenames = ["prices/{}".format(f) for f in os.listdir("prices")]
prices = pool.map(read_file, filenames)
prices = list(prices)
prices = dict(prices)

from dateutil.parser import parse

prices_columns = {}

for k,v in prices.items():
    price = v
    headers = price[0]
    price_columns = {}
    for i, header in enumerate(headers):
        values = [p[i] for p in price[1:]]
        if i > 0:
            values = [float(v) for v in values]
        else:
            values = [parse(v) for v in values]
        price_columns[header] = values
    prices_columns[k] = price_columns

from statistics import mean

average_closing = {}
for k,v in prices_columns.items():
    average_closing[k] = mean(v["close"])

closing_tuples = [(k,v) for k,v in average_closing.items()]
sorted(closing_tuples, key=lambda x:x[1])

trades = {}
for k, v in prices_columns.items():
    for i,date in enumerate(v["date"]):
        if date not in trades:
            trades[date] = []
        trades[date].append([k,v["volume"][i]]

most_traded = []
for k, v in trades.items():
    ordered = sorted(v, key=lambda x: x[1])
    symbol = ordered[-1][0]
    most_traded.append([k, symbol])
most_traded = sorted(most_traded, key=lambda x: x[0])

most_traded

daily_volumes = {}

most_traded = []
for k, v in trades.items():
    volume = sum([item[1] for item in v])
    daily_volumes[k] = volume

volume_tuples = [[k,v] for k,v in daily_volumes.items()]
volume_tuples = sorted(volume_tuples, key=lambda x: x[1])

volume_tuples[-10:]

import math

high_volume_days = [v[0] for v in volume_tuples[-10:]]

def binary_search(array, search):
    m = 0
    i = 0
    z = len(array) - 1
    while i<= z:
        m = math.floor(i + ((z - i) / 2))
        if array[m] == search:
            return m
        elif array[m] < search:
            i = m + 1
        elif array[m] > search:
            z = m - 1

high_volume_transactions = {}
for k,v in prices_columns.items():
    for day in high_volume_days:
        ind = binary_search(v["date"], day)
        if ind is None:
            continue
        if k not in high_volume_transactions:
            high_volume_transactions[k] = []
        high_volume_transactions[k].append(prices[k][ind])

profits = []
for k,v in prices_columns.items():
    percentage = (v["close"][-1] - v["close"][0]) / v["close"][0]
    profits.append([k,percentage * 100])

profits = sorted(profits, key=lambda x: x[1])

profits[-10:]
