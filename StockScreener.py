import time
from selenium import webdriver
import pandas as pd


symbols = ['CY', 'IBM', 'SC']
SelectedSymbols = []
for symbol in symbols:
    df = pd.read_csv('C:\\users\\shaima\\downloads\\' + symbol + '.csv')
    browser = webdriver.Chrome('C:\\Users\\shaima\\Downloads\\chromedriver.exe')
    browser.get('http://finance.yahoo.com/q/ks?s=' + symbol)

    BetaValue = browser.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]').text
    Beta = float(BetaValue)

    PriceValue = browser.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').text
    CurrentStockPrice = float(PriceValue)

    DebtToEquityRatioValue = browser.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[2]/div[5]/table/tbody/tr[4]/td[2]').text
    DebtToEquityRatio = float(DebtToEquityRatioValue)

    BookValuePerShareValue = browser.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[2]/div[5]/table/tbody/tr[6]/td[2]').text
    BookValuePerShare = float(BookValuePerShareValue)

    ReturnOnEquityValue = browser.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td[2]').text
    ReturnOnEquity = float(ReturnOnEquityValue.strip('%'))

    TotalCashPerShareValue = browser.find_element_by_xpath('//*[@id="Col1-0-KeyStatistics-Proxy"]/section/div[2]/div[1]/div[2]/div[5]/table/tbody/tr[2]/td[2]').text
    TotalCashPerShare = float(TotalCashPerShareValue)

    DailyDelta = browser.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').text

    print('_____________________________________________________________')
    print('                                                             ')
    print(symbol, 'went up/down', DailyDelta)
    print('Total Cash Per Share (mrq) = ', TotalCashPerShare)
    print('Return on Equity = ', ReturnOnEquity)
    print('Book Value Per Share = ', BookValuePerShare)
    print('Total Debt/Equity (mrq) = ', DebtToEquityRatio)
    print('Current Stock Price = ', CurrentStockPrice)
    print('Beta = ', Beta)


    if Beta > 1 and CurrentStockPrice < 100:
        SelectedSymbols.append(symbol)

print(SelectedSymbols)