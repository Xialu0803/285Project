import requests
import yfinance as yf
import random
import datetime as DT
import pandas as pd

stock_options = {
        'ethical': ['AAPL', 'ADBE', 'SBUX', 'GILD', 'GOOGL'],
        'growth': ['BIIB', 'PINS', 'IPGP', 'SFIX', 'NFLX'],
        'index': ['VTI', 'IXUS', 'ILTB', 'VIS', 'KRE', 'VEU'],
        'quality': ['QUAL', 'SPHQ', 'DGRW', 'QDF','SFR'],
        'value': ['AAON', 'TME', 'JNJ', 'GRUB', 'TTGT']
}

def suggest_stocks(amount, strategy_1):
    stock_info = []
    today = DT.date.today()
    week_ago = today - DT.timedelta(days=7)
    options = []
    perc = 0
    while len(options) < 3:
        temp = random.randint(0, 4)
        if temp not in options:
            options.append(temp)

    #print options
    i = 0
    for option in options:
        stock_list1 = stock_options[strategy_1]
        if i == 0:
            perc = 0.36
            i=i+1
        elif i == 1:
            perc = 0.24
            i=i+1
        elif i == 2:
            perc = 0.4

        temp = {}
        symbol = stock_list1[option]
        try:
            stock_name = yf.Ticker(symbol).info['shortName']
            #print(stock_list1[option])
            stock = yf.download(stock_list1[option], week_ago, today)
            #print(stock)
            stock = stock.values.tolist()

            temp["symbol"] = symbol
            temp["symbolName"] = stock_name
            temp['prices'] = [stock[0][3], stock[1][3], stock[2][3], stock[3][3], stock[4][3]]
            temp['investAmount'] = amount*perc
            temp['stocknumber'] = temp['investAmount']//stock[4][3]
            stock_info.append(temp)
        except Exception as e:
            print(e)
            return []

    return stock_info

if __name__ == "__main__":
    print("Please input the amount:")
    amount = int(input())
    while amount < 5000:
        print("The minimum invest amount is $5000 USD, please re-enter the amount:")
        amount = int(input())
    print("Please input the strategy,select from: ethical, growth, index, quality, value:")
    strategy = input()
    portfolio = suggest_stocks(amount, strategy)
    #print(portfolio)
    name1 = portfolio[0]["symbolName"]
    symbol1=portfolio[0]["symbol"]
    investAmount1= portfolio[0]["investAmount"]
    stockNum1=portfolio[0]["stocknumber"]

    name2 = portfolio[1]["symbolName"]
    symbol2 = portfolio[1]["symbol"]
    investAmount2 = portfolio[1]["investAmount"]
    stockNum2 = portfolio[1]["stocknumber"]

    name3 = portfolio[2]["symbolName"]
    symbol3 = portfolio[2]["symbol"]
    investAmount3 = portfolio[2]["investAmount"]
    stockNum3 = portfolio[2]["stocknumber"]
    print("The stocks chosen for strategy: "+strategy+" is: ")
    print("Stock Name:"+name1+" invest Amount:"+str(investAmount1)+" purchased number: "+str(stockNum1))
    print("Stock Name:"+name2+" invest Amount:"+str(investAmount2)+" purchased number: "+str(stockNum2))
    print("Stock Name:" + name3 + " invest Amount:" + str(investAmount3) + " purchased number: " + str(stockNum3))
    currentValue1= stockNum1*yf.Ticker(symbol1).info['regularMarketPrice']
    currentValue2= stockNum2 * yf.Ticker(symbol2).info['regularMarketPrice']
    currentValue3= stockNum3*yf.Ticker(symbol3).info['regularMarketPrice']
    print("current Value of the stock chosen: " )
    print("Stock Name:" + name1 + " Current Value Amount: " + str(currentValue1))
    print("Stock Name:" + name2 + " Current Value Amount: " + str(currentValue2))
    print("Stock Name:" + name3 + " Current Value Amount: " + str(currentValue3))
    print("total Current Value: "+str(currentValue1+currentValue2+currentValue3))
    print("------------------------------------------------------------------------------------------")
    print("Weekly trend of this strategy for the past 5 days")
    day1Price=portfolio[0]["prices"][0]*stockNum1+portfolio[1]["prices"][0]*stockNum2+portfolio[2]["prices"][0]*stockNum3
    day2Price = portfolio[0]["prices"][1] * stockNum1 + portfolio[1]["prices"][1] * stockNum2 + portfolio[2]["prices"][
        1] * stockNum3
    day3Price = portfolio[0]["prices"][2] * stockNum1 + portfolio[1]["prices"][2] * stockNum2 + portfolio[2]["prices"][
        2] * stockNum3
    day4Price = portfolio[0]["prices"][3] * stockNum1 + portfolio[1]["prices"][3] * stockNum2 + portfolio[2]["prices"][
        3] * stockNum3
    day5Price = currentValue1+currentValue2+currentValue3
    print("Day 1: "+str(day1Price))
    print("Day 2: " + str(day2Price))
    print("Day 3: " + str(day3Price))
    print("Day 4: " + str(day4Price))
    print("Day 5: " + str(day5Price))


