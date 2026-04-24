import tradingeconomics as te
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

te.login('')

## Please subscribe to a plan at https://tradingeconomics.com/api/pricing.aspx to get an API key.

## With no output_type defined, the result will be of the dictionary type.
## Use output_type='df' to display in pandas dataframe. 

# To get intraday P/E Ratio. Empty date returns the last P/E Ratio.
def getEarningsPerShareTTM(symbols=None, date=None, output_type=None):
    if date == None:
        date = str((datetime.now()).date())

    initDate = datetime.strptime(str(date), '%Y-%m-%d')
    initDate = str((initDate - relativedelta(years=1)).date())

    data = te.getEarnings(symbols=symbols, initDate=initDate, endDate=date, output_type='df')

    eps = data['Actual'].astype(float)
    eps = eps.sum()

    return eps

def getPERatio(symbols=None, date=None, endDate = None, output_type=None):
    if date != None:
        endDate = date

    data = pd.DataFrame(te.fetchMarkets(symbol=symbols, initDate=date, endDate=endDate, output_type='raw'))

    stockPriceLastRow = data.iloc[-1]
    
    eps = getEarningsPerShareTTM(symbols=symbols, date=date, output_type='df')

    peRatio = round(stockPriceLastRow['Close']/eps, 2)

    return peRatio

mydata = getPERatio(symbols='aapl:us', output_type='df')
print(mydata)
